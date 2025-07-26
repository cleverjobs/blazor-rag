# TelerikWindow within TelerikWindow

## Question

**Rob** asked on 14 Jan 2022

In the current version 2.30 Is it possible to create a component with containing a TelerikWindow (Modal=true) witch in turn also has another component containing another TelerikWindow (Modal=true), this last being opened when clicking for example on a button of the 1st component? So far several unsuccessful attempts (using Visible & VisibleChanged or @bind-Visible) 2nd window not displayed Seems to break the 1st one (close button not working anymore) No error displayed Thanks in advance.

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hello Robert, If the Close button does not work, this is likely an issue with passing data between the components. Perhaps a correct event is not raised from the child component and it gets the old value back as a parameter. The second most likely reason I can think of is that you are using a very old version where this scenario is not supported yet, you need to ensure you are on the latest (2.30.0 at the moment) or at the very least on 2.23.0. I made a basic sample for you that works fine for me: parent component: <TelerikWindow Modal="true" @bind-Visible="@isModal1Visible">
<WindowTitle>
<strong>The Title</strong>
</WindowTitle>
<WindowContent>
I am modal so the page behind me is not available to the user.

<TelerikButton OnClick="@( _=> isModal2Visible=true )">Open the SECOND window</TelerikButton>
<NestedComponent @bind-Visible="@isModal2Visible" />
</WindowContent>
<WindowActions>
<WindowAction Name="Minimize" />
<WindowAction Name="Maximize" />
<WindowAction Name="Close" />
</WindowActions>
</TelerikWindow>

<TelerikButton OnClick="@( _=> isModal1Visible=true )">Open the window</TelerikButton>

@code{ bool isModal1Visible { get; set; } bool isModal2Visible { get; set; }
} nested component: <h3>NestedComponent</h3>

<TelerikWindow Modal="true" Visible="@Visible" VisibleChanged="@VisibleChangedHandler">
<WindowTitle>
<strong>The SECOND Title</strong>
</WindowTitle>
<WindowContent>
SECOND ONE
</WindowContent>
<WindowActions>
<WindowAction Name="Minimize" />
<WindowAction Name="Maximize" />
<WindowAction Name="Close" />
</WindowActions>
</TelerikWindow>

@code{
[ Parameter ] public bool Visible { get; set; }
[ Parameter ] public EventCallback<bool> VisibleChanged { get; set; } async Task VisibleChangedHandler ( bool isVisible ) {
Visible=isVisible; await VisibleChanged.InvokeAsync(Visible);
}
} Regards, Marin Bratanov
