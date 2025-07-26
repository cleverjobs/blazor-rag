# How to trigger the upload from a parent component

## Question

**Hol** asked on 19 Apr 2022

Hi, I have the following structure (shortend): FormComponent.razor: <UploadBox @ref="@BoxForUpload" /> FormComponent.razor.cs: public UploadBox BoxForUpload;

public async Task OnSelect(UploadSelectEventArgs args)
{
BoxForUpload.DoUpload();
} UploadBox.razor: <TelerikUpload @ref="@UploadRef" AutoUpload="false"> </TelerikUpload> UploadBox.razor.cs: [ Parameter ] public EventCallback<UploadSelectEventArgs> OnSelect { get; set; } public TelerikUpload UploadRef { get; set; } public void DoUpload ( ) {
UploadRef.UploadFiles();
} If I set AutoUpload to true, the upload works. But if I set AutoUpload to false, the OnSelect will be triggered, but the upload do not work (no file receives the upload-api) and there are no errors in the console. How can I trigger the upload from the FormComponent?

## Answer

**Dimo** answered on 21 Apr 2022

Hi Holger, Use generic Blazor technique - see StackOverflow. Regards, Dimo Progress Telerik
