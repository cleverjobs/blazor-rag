# Resizing the Editor

## Question

**Oma** asked on 03 Feb 2024

Hello, I'm a newcomer to Telerik, and I'd appreciate it if you could assist me without suggesting that the documentation is clear enough. Is there an uncomplicated method to enable resizing for the Editor, similar to the one used in your forum's editor? I'm concurrently working with Syncfusion controls, and I've been able to implement a resizable editor easily using the code provided below with their control. How can I achieve the same functionality with your control? Regards, Omar @using Syncfusion.Blazor.RichTextEditor <div class="control-section resize"> <SfRichTextEditor EnableResize="true" Height="250px"> <p> The Rich Text Editor component is a WYSIWYG ("what you see is what you get") editor that provides the best user experience to create and update the content.
Users can format their content using standard toolbar commands. </p> </SfRichTextEditor> </div> <style>.e-richtexteditor { max-width: 880px; min-width: 200px; min-height: 170px; max-height: 400px;
}.control-section.resize.e-popup.e-popup-open.e-dialog { max-height: 410px!important;
} </style>

## Answer

**Omar** answered on 06 Feb 2024

I found a way to do that using CSS. <TelerikEditor @ref="Editor" Tools="@ToolCollection" @bind-Value="Description" class="myTelerikEditor" EditMode="@EditorEditMode.Div"> <EditorSettings> <EditorPasteSettings ConvertMsLists="true" RemoveMsClasses="true" RemoveMsStyles="true" RemoveHtmlComments="true" StripTags="@StripTags" RemoveAttributes="@RemoveAttributes"> </EditorPasteSettings> </EditorSettings> </TelerikEditor> The CSS .myTelerikEditor div.k-editor-content div.k-content { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: large; width: 100%; height: 200px; resize: vertical!important;
}.myTelerikEditor div.k-editor-content { min-height: 200px!important; max-height: 1000px!important; height: 100%!important;
}.myTelerikEditor { height: 100%; min-height: 200px!important; max-height: 1000px!important; height: 100%!important; resize: vertical!important;
}

### Response

**Hristian Stefanov** commented on 07 Feb 2024

Hi Omar, I'm happy to see you quickly resolved the matter on your own. Thank you for sharing it here, publicly, so other developers can benefit from it. Kind Regards, Hristian

### Response

**Stas** commented on 13 Aug 2024

Is there official support for resize property? This workaround above ignores the control's Height property. Thanks!

### Response

**Hristian Stefanov** commented on 14 Aug 2024

Hi Stas, We have an open feature request for the support of a resizable Editor: Resizable Editor. Upon interest, you can cast your vote there and raise the item's priority. You can also subscribe to the item to receive email notifications for further status updates. Kind Regards, Hristian
