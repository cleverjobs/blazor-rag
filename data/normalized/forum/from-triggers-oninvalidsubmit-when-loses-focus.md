# From triggers onInvalidSubmit when loses focus

## Question

**Car** asked on 12 Mar 2024

Hi, I have a situation where I want a button to be part of form which triggers a dialog to open on top so the user can choose an image via the filemanager component. Once selected I'll handle the binding to the form item to populate the details required for the form. However, when I have the button inside the form, and the user clicks it, the OnInvalidSubmit event is immediately triggered because the focus has now shifted to the dialog. Is there a way to disable this behavior? I would like the validation to only happen once the save button is pressed in this case. Thanks!

## Answer

**Nadezhda Tacheva** answered on 14 Mar 2024

Hi Carl, We've confirmed the root cause in your private ticket but I will add the information here for visibility in case other community members are hitting such an issue. The problem is related to the Button that triggers the Dialog and not that Form loses focus. The default Button type is Submit. You should configure the Type parameter in this scenario (e.g. set ButtonType.Button ), so clicking it does not submit the Form. Regards, Nadezhda Tacheva Progress Telerik
