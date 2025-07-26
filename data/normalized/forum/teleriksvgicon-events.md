# TelerikSvgIcon events

## Question

**Jos** asked on 09 Dec 2024

Unable to execute events on the TelerikSvgIcon control? <FormItem Field="@nameof(User.Password)"> <Template> <TelerikTextBox @bind-Value="@user.Password" Size="@ThemeConstants.TextBox.Size.Large" Placeholder="Contraseña" ShowSuffixSeparator="false" Password="@IsPasswordHidden"> <TextBoxSuffixTemplate> <TelerikSvgIcon Icon="@SvgIcon.Eye" Size="@ThemeConstants.SvgIcon.Size.Medium" onmousedown="@(()=> MostrarPassword())" onmouseup="@(()=> OcultarPassword())" onmouseleave="@(()=> OcultarPassword())"> </TelerikSvgIcon> </TextBoxSuffixTemplate> </TelerikTextBox> </Template> </FormItem> Thanks

## Answer

**Hristian Stefanov** answered on 09 Dec 2024

Hi José Antonio, To handle events with the TelerikSvgIcon, you need to wrap it in an element that supports event handlers, such as a span or div. The TelerikSvgIcon itself does not support direct event attributes like onmousedown, onmouseup, or onmouseleave. Solution <FormItem Field="@nameof(User.Password)"> <Template> <TelerikTextBox @bind-Value="@user.Password" Size="@ThemeConstants.TextBox.Size.Large" Placeholder="Contraseña" ShowSuffixSeparator="false" Password="@IsPasswordHidden"> <TextBoxSuffixTemplate> <span style="cursor: pointer;" onmousedown="@(()=> MostrarPassword())" onmouseup="@(()=> OcultarPassword())" onmouseleave="@(()=> OcultarPassword())"> <TelerikSvgIcon Icon="@SvgIcon.Eye" Size="@ThemeConstants.SvgIcon.Size.Medium"> </TelerikSvgIcon> </span> </TextBoxSuffixTemplate> </TelerikTextBox> </Template> </FormItem> Regards, Hristian Stefanov Progress Telerik
