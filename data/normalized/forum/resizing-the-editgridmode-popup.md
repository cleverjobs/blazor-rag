# Resizing the EditGridMode Popup?

## Question

**And** asked on 19 May 2020

Hello! Is there a way to resize the modal window from Editable="EditGridMode.Popup" on a DataGrid? I did find [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form) via another forum thread, but that seems like wild overkill just to change the size of the modal by like 50px. Thanks, Andrew

## Answer

**Marin Bratanov** answered on 20 May 2020

Hello Andrew, Right now the Window component itself is not resizable (or draggable). It is likely that once those features are implemented there, they may become available in the grid popup too. The grid popup does not have a set height, so it will stretch to accommodate the fields. With too many fields it can go off the screen and a fix for that will come through this: [https://feedback.telerik.com/blazor/1460670-grid-popup-edit-window-is-not-responsive-and-goes-off-the-screen](https://feedback.telerik.com/blazor/1460670-grid-popup-edit-window-is-not-responsive-and-goes-off-the-screen) That said, for customized layouts, the custom form is the solution. For example, see also this feature request: [https://feedback.telerik.com/blazor/1456950-change-the-title-in-editing-popup](https://feedback.telerik.com/blazor/1456950-change-the-title-in-editing-popup) With this information in mind, if you would like to see a built-in feature in the grid that is not available right now, I would encourage you to post a feature request for such a feature in our Feedback portal through the "Request a Feature" button. Just make sure to select the "make public" checkbox at the final step. This will let you explain your goals, requirements, even perhaps add a sample of what API and functionality you would expect it exposes. You can then Vote for it and Follow it to get updates on status changes. If it gets good traction with the community, we will consider its implementation. Regards, Marin Bratanov

### Response

**Andrew** answered on 20 May 2020

(If you could possibly delete the previous post, that'd be great! Wrong file attached)

### Response

**Marin Bratanov** answered on 20 May 2020

Hello Andrew, I deleted the previous post. The issue here is that the Kendo LESS themes are not supported for Blazor. You should use only one of the themes that comes with our Blazor offering Default, Bootstrap and Material themes: [https://docs.telerik.com/blazor-ui/themes/overview](https://docs.telerik.com/blazor-ui/themes/overview) The BlueOpal theme is not among them and you should not mix them (read more here: [https://docs.telerik.com/blazor-ui/knowledge-base/jquery-kendo-in-blazor](https://docs.telerik.com/blazor-ui/knowledge-base/jquery-kendo-in-blazor) ). Regards, Marin Bratanov

### Response

**Andrew** answered on 20 May 2020

I appreciate your quick responses, Marin. The instructions for using the ReportViewer in Blazor specify to use those themes (see [https://docs.telerik.com/reporting/blazor-report-viewer-how-to-use](https://docs.telerik.com/reporting/blazor-report-viewer-how-to-use) ). Is this documentation outdated? I tried not using those themes, but then the ListView component for my parameters doesn't highlight the selected item. Thanks again, Andrew

### Response

**Marin Bratanov** answered on 21 May 2020

Hi Andrew, Thank you for noticing. I opened an issue so that this gets fixed and you can see it here [https://github.com/telerik/reporting-docs/issues/114.](https://github.com/telerik/reporting-docs/issues/114.) In the meantime, please try removing the LESS theme (BlueOpal or whichever one you are using) and add one of the SASS themes (say, Default2) as explained here: [https://docs.telerik.com/blazor-ui/themes/overview](https://docs.telerik.com/blazor-ui/themes/overview) On a side note - the ListView component does not have a selection feature, that's something you should implement through your own onclick event on the item template and its own class. Regards, Marin Bratanov
