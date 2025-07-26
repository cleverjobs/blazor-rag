# Why doesn't this code produce a round button like in the demo?

## Question

**Dav** asked on 11 Feb 2022

<GridToolBar>
<AuthorizeView Roles="DOMAIN\GROUP">
<Authorized>
<GridCommandButton Command="Add" Icon="add">Add Permission</GridCommandButton>
</Authorized>
</AuthorizeView>
<TelerikButton OnClick="@_reloadPermissions" Enabled="@_reloadEnabled" FillMode="@(ThemeConstants.Button.FillMode.Solid)" Rounded="@(ThemeConstants.Button.Rounded.Full)" Shape="@(ThemeConstants.Button.Shape.Square)" ThemeColor="@(ThemeConstants.Button.ThemeColor.Primary)" Size="Medium">
<TelerikIcon Icon="arrow-rotate-cw" />
</TelerikButton>
</GridToolBar> Instead I get this: I want the second button to be a round "refresh" button.

## Answer

**Svetoslav Dimitrov** answered on 21 Feb 2022

Hello David, I would like to offer two different solutions: If you are using a custom theme built through the Telerik ThemeBuilder I would suggest you upload that theme to the ThemeBuilder and just download it again. This would update the theme and add the styles for the component options. If you used VSX to add the Telerik UI for Blazor, the extension would add a local copy of the theme in the wwwroot folder. If this is the case you should manually replace that copy of the theme. Let me know if any of these suggestions helped you move forward. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Svetoslav Dimitrov** answered on 15 Feb 2022

Hello David, If you are using the CDN to retrieve the themes you should upgrade the CDN link according to the new one for the 3.0.0 release. You can find more information here. If this is not the case I would suggest you follow the upgrade procedure again as something might have gone wrong. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**David** commented on 16 Feb 2022

I am not using the CDN. I am using the Nuget package. I uninstalled the Telerik UI for Blazor NuGet package and re-installed it but the issue persists. What else can I do to troubleshoot the upgrade process?
