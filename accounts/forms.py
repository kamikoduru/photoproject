from django.contrib.auth.forms import UserCreationForm
# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
        # 連携するUserモデルを設定
        class Meta:
                model = CustomUser
                # フォームで使用するフィールドを設定
                # ユーザー名、メールアドレス、パスワード、パスワード(確認用)
                fields = ('username', 'email', 'password1', 'password2')