# box-shadow on k-animation-container class

## Question

**Jef** asked on 07 Mar 2021

I know there was already a discussion about how the k-animation-container was hiding the box-shadow and by adjusting the padding/margins, the shadow could be revealed. I'm attempting to approach this from a different perspective. I've applied a box-shadow to the k-animation-container itself and it looks fine except for the fact that the shadow appears immediately... before the animation of the dropdown starts. This results in the drop-down list appearing to slide into the shadow. I see the same behavior with the DatePicker and ComboBox. I see that there is a k-animation-container-shown class as well but it doesn't appear to be implemented. At least not with the DropDownList. As a matter of fact, I've discovered that k-animation-container-shown is used with the ContextMenu but even then not as I would expect. With the ContextMenu, the k-animation-container-shown class is applied to the div element even when the menu isn't visible...but, it gets the job done as the menu appears with the shadow instantly. The ContextMenu isn't animated into position. (Not sure if that's something you are planning on doing in the future.) I was hoping the k-animation-container-shown class would be consistently applied to the div once the DropDownList/ContextMenu/DateTimePicker was fully visible (i.e. at the end of the animation). Any suggestions on how to best apply the shadow to all of the controls? Another solution would be to just get rid of the animation. Doesn't look like I can do that with a parameter on the control. How would I best override the animation?

## Answer

**Marin Bratanov** answered on 08 Mar 2021

Hi Jeffrey, If you are referring to the Material Theme lacking a shadow on the dropdowns, you can Follow its fix here: [https://feedback.telerik.com/blazor/1428679-popups-like-filter-menu-dropdownlist-do-not-have-a-border-shadow-in-material-theme.](https://feedback.telerik.com/blazor/1428679-popups-like-filter-menu-dropdownlist-do-not-have-a-border-shadow-in-material-theme.) You can also remove animations with CSS for the time being, and you can Follow a more "programmatic" way here: [https://feedback.telerik.com/blazor/1469662-way-to-modify-default-values-of-animations-such-as-duration-and-delay-for-a-component-such-as-combobox.](https://feedback.telerik.com/blazor/1469662-way-to-modify-default-values-of-animations-such-as-duration-and-delay-for-a-component-such-as-combobox.) Regards, Marin Bratanov

### Response

**Jeffrey** answered on 08 Mar 2021

Thanks Marin... I didn't realize it was limited to the Material theme. I was aware of the fix and have already applied the box-shadow on the k-animation-container class. The one drawback to that solution is that the shadow appears before the animation is complete. The animation is a nice-to-have but not critical so I went ahead and overrode the transition setting on the k-popup class as you suggested. Unfortunately, there is still one minor visual glitch with that approach. There seems to be a delay after the popup closes, such that the shadow remains visible for a second after the popup disappears. I haven't been able to figure out what's causing that.

### Response

**Marin Bratanov** answered on 08 Mar 2021

Hi Jeffrey, These things are much harder to hack like that in Blazor since there isn't direct control over the DOM (when comparing to things like Kendo UI for jQuery). Until the actual features get implemented, I'm afraid I can't offer better options. Regards, Marin Bratanov

### Response

**Jeffrey** answered on 08 Mar 2021

No worries! Thanks for the quick reply.
