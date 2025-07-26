# Z-index inconsistency when ContextMenu is invoked manually vs via Selector

## Question

**Jef** asked on 07 Jan 2022

I've got a ContextMenu that is invoked by clicking a button ... it is not invoked via the Selector property of the ContextMenu. <div class="d-flex k-align-items-center justify-content-center icon-button" title="Download" id="download-menu" @oncontextmenu:preventDefault="true" @onclick="((MouseEventArgs e)=> ShowDownloadMenu(e))"> <i class="fad fa-file-download"> </i> Download </div> <TelerikContextMenu @ref="@DownloadMenu" Data="@DownloadMenuItems" OnClick="@((MenuItem item)=> DownloadMenuHandler(item))"> </TelerikContextMenu> Here's where the menu is invoked: private async Task ShowDownloadMenu ( MouseEventArgs e ) { if (e.Button==0 )
{ await DownloadMenu.ShowAsync(e.ClientX, 45 );
}
} When the context menu is invoked via code, the z-index value comes from .k-animation-container and is set to 100. As you can see, the menu is not given an explicit z-index value: <div class="k-animation-container telerik-blazor k-widget k-animation-container-shown" data-id="94f3d3b5-3db1-4940-ab74-c03895eeeaa2" id="94f3d3b5-3db1-4940-ab74-c03895eeeaa2" style="width: auto; left: 554px; top: 45px;" This is fine in most cases except when the ContextMenu is within a Window component, in that case the menu is displayed behind the window. If the same context menu is invoked by way of the Selector property on the ContextMenu and a right-click, it is given an explicit z-index value (in this case 10003), such that it will display in front of the Window component: <div class="k-animation-container telerik-blazor k-widget k-animation-container-shown" data-id="e0cd095f-32f8-40a5-af0b-0e0ddc2a0f71" id="e0cd095f-32f8-40a5-af0b-0e0ddc2a0f71" style="width: auto; z-index: 10003; top: 81px; left: 556px;"> I've tried to override the z-index by adding a Class to the ContextMenu but the class gets added to an inner <div>, not the topmost <div> so the z-index is useless. I've tested a brute force solution by overriding z-index on the .k-animation-container class and it seems to work but it feels like overkill.

## Answer

**Marin Bratanov** answered on 08 Jan 2022

Hello Jeffrey, Thank you for this report, I logged it for fixing and you can track it with this page: [https://feedback.telerik.com/blazor/1548718-showing-the-context-menu-via-its-api-method-does-not-set-its-z-index](https://feedback.telerik.com/blazor/1548718-showing-the-context-menu-via-its-api-method-does-not-set-its-z-index) - it also contains a link to the potential workaround -a bit of a CSS hack that I intentionally keep behind the link to make sure people read the implication - that it will affect all animation containers on the site. Regards, Marin Bratanov
