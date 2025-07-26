# Popup Width

## Question

**Phi** asked on 22 Jan 2020

Does anyone know of a way to force the ComboBox Popup to have an equal width to the ComboBox itself? My ComboBox doesn't have a fixed width like 300px because I am using it within a Bootstrap column. I have tried setting the Popup width to 100% but that makes it 100% of the whole page not 100% of the ComboBox width. There are some ways I can fudge the Popup width so that it is close to the ComboBox width, but I am looking for a way to have it always match the ComboBox width regardless of the ComboBox size. Any help would be appreciated!

## Answer

**Marin Bratanov** answered on 22 Jan 2020

Hi Phil, We intend to have the dropdown components behave like that out-of-the-box. You can Follow the status of this feature here: [https://feedback.telerik.com/blazor/1440092-dropdown-components-to-calculate-their-dropdown-element-width-to-match-the-actual-width-of-the-component-in-px-when-popupwidth-is-not-set.](https://feedback.telerik.com/blazor/1440092-dropdown-components-to-calculate-their-dropdown-element-width-to-match-the-actual-width-of-the-component-in-px-when-popupwidth-is-not-set.) I added your Vote for it to raise its priority (you can also Vote yourself for features you want to see implemented, or open new feature requests). The behavior you see is expected, and if you set PopupWidth="100%" even after that feature is implemented you would get the same behavior. Here are more details on that: [https://docs.telerik.com/blazor-ui/common-features/dimensions](https://docs.telerik.com/blazor-ui/common-features/dimensions) If you are looking for a kind of responsive behavior on the dropdown, I can also suggest you consider something like this where the dropdown adjusts to the contents. It is a different behavior and auto height is not suitable for many elements, but it can provide a measure of tightness around the content. <TelerikDropDownList Data="@MyList" @bind-Value="MyItem" PopupWidth="auto" PopupHeight="auto">
</TelerikDropDownList>

@code { protected List<string> MyList=new List<string>() { "first", "lorem ipsum dolor sit amet", "third" }; protected string MyItem { get; set; }="third";
} Regards, Marin Bratanov

### Response

**Phil** answered on 22 Jan 2020

Hi Marin, Thank you for the information! Very excited to see this feature along with the other approved and planned features.

### Response

**Doug** answered on 21 May 2020

Along these same lines, I'm trying to figure out how to get the combobox to be the same width as the content. Or as wide as the widest entry in the drop down list. Setting PopupWidth=auto works great for the drop down list, but what about the combobox itself? Setting Width=auto doesn't have much effect. Is this possible?

### Response

**Svetoslav Dimitrov** answered on 22 May 2020

Hello Doug, This feature was completed with our 2.13.0 release as you can see from our Feedback Portal ( [https://feedback.telerik.com/blazor/1440092-dropdown-components-to-calculate-their-dropdown-element-width-to-match-the-actual-width-of-the-component-in-px-when-popupwidth-is-not-set](https://feedback.telerik.com/blazor/1440092-dropdown-components-to-calculate-their-dropdown-element-width-to-match-the-actual-width-of-the-component-in-px-when-popupwidth-is-not-set) ). I would suggest you upgrade ( [https://docs.telerik.com/blazor-ui/upgrade/overview](https://docs.telerik.com/blazor-ui/upgrade/overview) ) to that version or our latest (2.14.0 at the time of writing this) so you can take advantage of this feature. If you already have upgraded and this issue still persist you can open a Support ticket where so we can further investigate the issue. Regards, Svetoslav Dimitrov

### Response

**Doug** answered on 22 May 2020

Ah, sorry, I thought I was current but I was on 2.10. With 2.14 it works better but if you select the longest entry in the list it chops off the last couple characters when selected. So I guess for now I'll still have to set a sufficiently large width value. Thanks for the response.

### Response

**Marin Bratanov** answered on 24 May 2020

Hi Doug, In such cases, it would be up to the application developer to choose - the dropdowns cannot handle both scenarios automatically at the same time. At the moment, the dropdown element is as wide as the main element in case you don't set an explicit DropDownWidth. This has been commonly requested as it greatly improves the UX for responsive layouts. When you have very long texts, however, you may want to keep using DropDownWidth="auto" so the browser will fit the dropdown element to its contents. This DropDownWidth setting and behavior applies to all dropdown components - the combobox, the dropdownlist, the multiselect and the autocomplete. Regards, Marin Bratanov

### Response

**Ivan** answered on 13 Jan 2021

We sort of figured out the width, but what to do with the height? I just can't limit the maximum height of the drop-down list, when setting the height to auto, the list is very large, there are many entries. Is there a custom css class where max-height and overflow-y can be set?

### Response

**Marin Bratanov** answered on 13 Jan 2021

Hello Ivan, Our upcoming 2.21.0 release will have PopupClass on all dropdown components so you could cascade such rules per instance (such as min-width, or max-height), without breaking all other popups/dropdowns in your app. For anyone else interested in some sort of automatic witdh setup, you can Vote for and Follow this request: [https://feedback.telerik.com/blazor/1501524-add-autowidth-parameter.](https://feedback.telerik.com/blazor/1501524-add-autowidth-parameter.) Regards, Marin Bratanov

### Response

**Ivan** answered on 13 Jan 2021

Great news, many thanks!
