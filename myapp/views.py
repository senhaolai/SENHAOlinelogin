# myapp/views.py

from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.http import JsonResponse
from django.urls import reverse
from .linepay_client import line_pay_api
import time

from myapp.forms import UserProfileForm  # Assuming your form is in myapp.forms

def user_profile(request):
    social_account = SocialAccount.objects.get(user=request.user)
    initial_data = {
        'uid': social_account.uid,
        'extra_data': social_account.extra_data,
        'user': social_account.user,
    }
    form = UserProfileForm(initial=initial_data)
    return render(request, 'profile.html', {'form': form})

def user_profile1(request):
    # 從 SocialAccount 中取得當前使用者的社交媒體帳戶資訊
    social_account = SocialAccount.objects.get(user=request.user)

    # 從社交媒體帳戶的 extra_data 中解析出所需的資訊
    extra_data = social_account.extra_data
    name = extra_data.get('name', '')  # 從 extra_data 中取得名稱，如果不存在則設為空字串
    email = extra_data.get('email', '')  # 從 extra_data 中取得電子郵件，如果不存在則設為空字串
    picture_url = extra_data.get('picture', '')  # 從 extra_data 中取得頭像 URL，如果不存在則設為空字串

    # 準備要傳遞給模板的上下文（context）資料
    context = {
        'name': name,
        'email': email,
        'picture_url': picture_url,
    }

    # 使用 render 函式將上下文資料傳遞給 profile.html 模板，並返回 HTTP 響應
    return render(request, 'profile.html', context)







# line pay  的請求
def initiate_payment(request):
    # 使用当前时间戳生成唯一的订单编号
    order_id = f'order_{int(time.time())}'  # 可以根据需要调整格式
    payment_params = {
        'amount': 1,  # 付款金額
        'currency': 'TWD',  # 貨幣代碼
        'orderId': 'order_id',  # 訂單編號
        'packages': [  # 必須包含商品包信息
            {
                'id': 'package1',
                'amount': 1,
                'name': 'Sample Package',
                'products': [
                    {
                        'name': 'Sample Product',
                        'quantity': 1,
                        'price': 1
                    }
                ]
            }
        ],
        'redirectUrls': {  # 使用新的鍵名 'redirectUrls' 來替換 'confirmUrl'
            'confirmUrl': request.build_absolute_uri(reverse('confirm_payment')),
            'cancelUrl': request.build_absolute_uri(reverse('initiate_payment'))
        }
    }
    
    try:
        response = line_pay_api.request(payment_params)
        if response['returnCode'] == '0000':
            return redirect(response['info']['paymentUrl']['web'])
        else:
            return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'error': str(e)})

# line pay  的回調
def confirm_payment(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transactionId')
    elif request.method == 'GET':
        transaction_id = request.GET.get('transactionId')
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    

    if not transaction_id:
        return JsonResponse({'error': 'Missing transactionId parameter'})
    try:

        amount = 1.0  # 需要与发起支付时的金额一致
        currency = 'TWD'  # 需要与发起支付时的货币一致
        response = line_pay_api.confirm(int(transaction_id), amount, currency)
        return JsonResponse(response)
    
    # except ValueError:
    #     return JsonResponse({'error': 'Invalid transactionId format'})
    except Exception as e:
        print(f"Received error: {str(e)}")  # 添加调试输出
        return JsonResponse({'error': str(e)})

