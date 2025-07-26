# Blazor Word processor

## Question

**Olt** asked on 09 Apr 2024

We are in search of a word processor component for Blazor, that delivers a user experience comparable to word processors such as Google Docs, DevExpress, or Syncfusion. Our core requirements include features document formatting (page size, orientation, etc), importing docx, saving as docx. Could you provide insight into whether TelerikEditor, coupled with appropriate word processing libraries, is capable of achieving this level of functionality? Thank you.

## Answer

**Dimo** answered on 12 Apr 2024

Hi Oltețeanu, The Blazor Editor can be used as an HTML editor and it can also be integrated with Telerik Document Processing for HTML manipulation that is not supported by the Editor itself and possible custom tools. You can also check this sample app about Editor import and export. However, the Editor component is focused on web content and doesn't have a notion for paper pages or page orientation. It cannot show the HTML content page by page like MS Word would. For this, we have a feature request for another component - the Rich Text Editor. Regards, Dimo Progress Telerik
