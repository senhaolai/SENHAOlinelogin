# myapp/forms.py

from django import forms # 導入 Django 的表單框架，用於定義表單。
from allauth.socialaccount.models import SocialAccount

# 直接使用 Django Allauth 提供的 SocialAccount 模型。然後創建一個表單來呈現這些資料。

class UserProfileForm(forms.ModelForm): # 定義了一個名為 UserProfileForm 的表單類別，它繼承自 forms.ModelForm，這表示它是基於模型的表單，可以直接與模型進行交互。
    class Meta: # 內部的 Meta 類別用於提供一些元資料給 Django，幫助它理解如何處理這個表單類別。
        model = SocialAccount # 這個屬性指定了表單類別要和哪個模型進行關聯。在這裡，UserProfileForm 與 SocialAccount 模型進行了關聯，這意味著當表單被提交時，它將用來創建或更新 SocialAccount 的實例。
        fields = ['uid', 'extra_data', 'user'] # 這個屬性指定了哪些模型的欄位應該被包含在表單中。在這裡，表單包括了 SocialAccount 模型中的 uid、extra_data 和 user 這三個欄位。
