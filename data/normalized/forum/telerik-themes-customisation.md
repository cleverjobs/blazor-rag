# Telerik Themes Customisation

## Question

**Ric** asked on 10 Oct 2022

Hi, We build a custom CSS file that includes the SCSS for the components we use as described in [https://docs.telerik.com/blazor-ui/styling-and-themes/custom-theme#using-the-build-process-of-the-application](https://docs.telerik.com/blazor-ui/styling-and-themes/custom-theme#using-the-build-process-of-the-application) However, I have noticed that there are classes that only exist in the @progress/kendo-theme-default/dist/all.scss file. One example is.k-overflow-auto which is used by the PDF viewer component without which the component does not display correctly and the paging functionality does not work. This suggests it is not currently possible to use the customisation method to reduce the size of the delivered CSS as not all the classes will be available. Or have I missed something? Cheers, R.

## Answer

**Nadezhda Tacheva** answered on 13 Oct 2022

Hi Richard, Thank you for reaching out! I've revised the case with our front-end engineers. It appears that this class is indeed missing when importing just the PDF Viewer SCSS. Let me provide some details on the root cause, how you can handle that and the further steps we will take on the matter: Root cause When you are importing only the source for the PDFViewer, you are essentially getting the following: [https://github.com/telerik/kendo-themes/blob/develop/packages/default/scss/pdf-viewer/_index.scss](https://github.com/telerik/kendo-themes/blob/develop/packages/default/scss/pdf-viewer/_index.scss) It will then import the needed styles for the separate elements of the PDFViewer. However, the dependencies list in it is currently missing the utils file which is responsible for introducing the .k-overflow-auto class: [https://github.com/telerik/kendo-themes/blob/0201d4902835ab5e2fde7f00d42fed5b2e3b3dff/packages/default/scss/utils/README.md#overflow](https://github.com/telerik/kendo-themes/blob/0201d4902835ab5e2fde7f00d42fed5b2e3b3dff/packages/default/scss/utils/README.md#overflow) Further steps I've logged a bug report in the kendo-themes-repo, so our front-end engineers can address that and add the needed dependency: PDFViewer SCSS is missing the utils dependency Workaround For the time being, it is possible to only import the PDFViewer source in order to reduce the size of the delivered CSS. However, you will need to manually import the utils like so: @import "~@progress/kendo-theme-default/scss/utils/_index.scss"; Last but not least, I'd like to thank you for your report! As s small gesture of gratitude, I have rewarded your account with some Telerik points. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Richard** commented on 13 Oct 2022

Many thanks Nadezhda. I'll track that bug report so I can remove the utils import workaround at a later date. Cheers, R.
