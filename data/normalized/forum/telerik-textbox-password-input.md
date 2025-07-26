# Telerik Textbox Password Input

## Question

**Ant** asked on 12 Feb 2024

Is there a way to keep the show password icon on the textbox whether the textbox is focused or not or when its initialized?

## Answer

**Dimo** answered on 15 Feb 2024

Hi Anthony, I assume that you are using the input adornments that we released in 5.1.0. You can implement something like the approach below. When we implement a built-in focus event, you may be able to use it as well. <span @onfocusin="@OnTextBoxFocus" @onfocusout="@OnTextBoxBlur"> <TelerikTextBox @bind-Value="@Password" Width="200px" Password="@MaskPassword"> <TextBoxSuffixTemplate> @if (ShowEyeIcon)
{ <TelerikButton Icon="@( MaskPassword ? SvgIcon.Eye : SvgIcon.EyeSlash )" FillMode="@ThemeConstants.Button.FillMode.Flat" OnClick="@( ()=> MaskPassword=!MaskPassword )" /> } </TextBoxSuffixTemplate> </TelerikTextBox> </span>

@code {
string Password { get; set; }="foo";

bool ShowEyeIcon { get; set; }

bool MaskPassword { get; set; }=true; void OnTextBoxFocus ( ) {
ShowEyeIcon=true;
} void OnTextBoxBlur ( ) {
ShowEyeIcon=false;
}
} Regards, Dimo Progress Telerik
