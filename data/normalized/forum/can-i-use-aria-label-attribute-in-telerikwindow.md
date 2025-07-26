# Can I use aria-label attribute in TelerikWindow?

## Question

**Ale** asked on 01 Mar 2023

I need aria-label (for accessibility) but when I add it to TelerikWindow: <TelerikWindow @ref="myWindow" Header="My Window" Width="300" Height="200" aria-label="My Custom Label"> but getting the following error: System.InvalidOperationException: Object of type 'Telerik.Blazor.Components.TelerikWindow' does not have a property matching the name 'aria-label'. The same if I try to add AdditionalAttributes <TelerikWindow @ref="myWindow" Header="My Window" Width="300" Height="200" AdditionalAttributes="@windowAttributes">
<Content>
<div class="window-content">
<p>This is my window content.</p>
</div>
</Content>
</TelerikWindow>

@code { private Dictionary<string, object> windowAttributes=new Dictionary<string, object> { { "aria-label", "My Custom Label" } }; private TelerikWindow myWindow;
} How I can add aria-label to TelerikWindow?

## Answer

**Svetoslav Dimitrov** answered on 06 Mar 2023

Hello Alexandre, I have opened a new feature request on your behalf - Add the AriaLabelledBy and AriaDescribedBy parameters. I have added your Vote for it and you are automatically subscribed to receive email notifications on status updates. On the topic of the aria-label - according to the MDN web docs, the aria-label is not supported for role="dialog". Regards, Svetoslav Dimitrov

### Response

**Alexandre** commented on 06 Mar 2023

Thank you! Can we also have attribute aria-modal="true" and attribute role=dialog?

### Response

**Svetoslav Dimitrov** commented on 09 Mar 2023

Hello Alexandre, We already add the aria-modal="true/false", and the role="attribute". When the Modal parameter of the TelerikWindow is set to true the aria-modal becomes true, as well, else it remains false. The role attribute is always set to dialog no matter the value of the Modal parameter. These attributes already comply with the accessibility standards That being said, do you believe you still believe you need to modify them?

### Response

**Alexandre** commented on 09 Mar 2023

ok, I see them now
