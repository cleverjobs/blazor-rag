# TextBox PlaceHolder color

## Question

**Ila** asked on 28 Jun 2022

How can I change the PlaceHolder inner text color? Nothing seems to be working... <TelerikTextBox Value="@_searchVariable" PlaceHolder="Search Variables" ValueChanged="@(BuildTree)"></TelerikTextBox>

## Answer

**Dimo** answered on 30 Jun 2022

Use::placeholder with higher specificity (to override our theme styles ): span.k-input::placeholder, span.k-picker::placeholder { color: red;
}
