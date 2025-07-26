# How to set small for all controls

## Question

**Mar** asked on 04 Oct 2023

Is there a way to set small "sm" for all controls global? so I can avoid <TelerikGrid Data=" @ChildCores " Size="sm"

## Answer

**Dimo** answered on 09 Oct 2023

Hello Martin Herløv, You can use a CascadingParameter for that. We have a few requests for built-in global settings and when we decide to implement them, the Size will probably be included as well. Global AdaptiveMode Global animation Global ThemeColor Regards, Dimo Progress Telerik

### Response

**Martin Herløv** answered on 09 Oct 2023

I not sure how to implement it. This is what I have tried and it's not working. In Mainlayout @inherits LayoutComponentBase

<TelerikRootComponent>
<UpdateAvailableDetector/>
<div class="sidebar bg-dark" style="min-width: 250px">
<NavMenu/>
</div>

<div class="main">
<TelerikNotification @ref="@Notification.Instance" HorizontalPosition="@NotificationHorizontalPosition.Center" VerticalPosition="@NotificationVerticalPosition.Top" Class="bi-notification">
</TelerikNotification>
<TelerikLoaderContainer Visible="@ProgressIndicator.Visible" Text="Working on it .." Size="@ThemeConstants.Loader.Size.Large" />
<CascadingValue IsFixed="true" Value="@Notification">
<CascadingValue Value="@ProgressIndicator">
<CascadingValue IsFixed="true" Value="@Size" Name="Size">
<div class="content">
@Body
</div>
</CascadingValue>
</CascadingValue>
</CascadingValue>
</div>
</TelerikRootComponent>

@code{ private const string Size="sm";
Notification Notification { get; }=new ();
ShowProgressIndicator ProgressIndicator { get; }=new ();
} The parameter Size in the grid is not picking up the Size parameter.

### Response

**Dimo** commented on 09 Oct 2023

Martin Herløv - can you confirm that you are actually consuming the cascading parameter in the Grid? This works on my side: The Grid Size is: @Size

<TelerikGrid Size="@Size" />

@code {
[CascadingParameter(Name="Size" )]
public string Size { get; set; }
}
