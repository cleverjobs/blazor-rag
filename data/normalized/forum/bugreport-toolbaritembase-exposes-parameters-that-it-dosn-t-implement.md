# Bugreport ToolBarItemBase exposes Parameters that it dosn't implement

## Question

**Lar** asked on 13 Jan 2025

ToolBarItemBase exposes Class and other Parameters via it's inheritance, but dosn't implement them. This causes problems when you want to for example add Class="k-grow" in the ToolBarTemplateItem and TelerikTextBox to make if swell and fill the toolbars remaining space. Sample Code: @page "/home" <TelerikToolBar> <ToolBarTemplateItem Class="This-Class-Is-Not-Rendeder-In-Browser-DOM"> <TelerikTextBox Class="This-Class-Works-Fine" /> </ToolBarTemplateItem> </TelerikToolBar> DOM: <main class="main" b-29r974uz1l=""> <div class="k-toolbar telerik-blazor k-toolbar-resizable k-toolbar-md" role="toolbar" data-id="e665969e-a55f-4bb1-8503-427f659bc6ab" dir="ltr"> <div class="k-toolbar-item" tabindex="0"> <span class="k-textbox k-input This-Class-Works-Fine telerik-blazor k-input-solid k-rounded-md k-input-md"> <input role="textbox" id="8152979c-ef9b-47f2-9315-acdc5fb5ac38" data-id="a24df6d2-8ce8-4ee3-bd68-3d27283b8bfd" class="k-input-inner" dir="ltr" aria-readonly="false" tabindex="0"> </span> </div> <button class="telerik-blazor k-button k-toolbar-overflow-button k-hidden k-button-flat k-rounded-md k-button-md k-button-flat-base k-icon-button" data-id="1aeae0a0-1a66-404e-914d-2cd4ddba222d" dir="ltr" tabindex="-1" title="More tools" aria-disabled="false" type="button"> <span class="telerik-blazor k-button-icon k-icon k-svg-icon k-svg-i-more-vertical" aria-hidden="true"> <svg xmlns:xlink="[http://www.w3.org/1999/xlink"](http://www.w3.org/1999/xlink") xmlns="[http://www.w3.org/2000/svg"](http://www.w3.org/2000/svg") viewBox="0 0 512 512"> <path d="M240 128c26.4 0 48-21.6 48-48s-21.6-48-48-48-48 21.6-48 48 21.6 48 48 48m0 64c-26.4 0-48 21.6-48 48s21.6 48 48 48 48-21.6 48-48-21.6-48-48-48m0 160c-26.4 0-48 21.6-48 48s21.6 48 48 48 48-21.6 48-48-21.6-48-48-48"> </path> </svg> </span> </button> </div> </main> ToolBarTemplateItem.razor from your source code dosn't seem to have any actual implementation for this in the razor file, nor do I see any BuildRenderTree functions in any of the inhertied classes. I assume this is the problem. Or am I missing something? @namespace Telerik.Blazor.Components

@inherits ToolBarItemBase

## Answer

**Hristian Stefanov** answered on 13 Jan 2025

Hi Lars, A bug report for the described behavior has already been submitted on our public feedback portal: The Class parameter of the ToolBarTemplateItem, ToolBarButton, and ToolBarSeparator is not getting applied. I voted for the item on your behalf and raised its priority. You can also subscribe to receive email notifications for status updates. Possible Workaround In the meantime, you can use different CSS selectors in order to style the specific elements. See the description of the above-linked item. Regards, Hristian Stefanov Progress Telerik

### Response

**Lars** commented on 15 Jan 2025

Thank you for the issue link and upvote. The workaround is not possible for us however, since we need to apply flex-box rules for our elements. And if we can't target every element in the chain it becomes a blocker that kills the "flex-grow chain". I managed to sort it eventually using some ::deep targeting, but it's hardly an optimal solution.
