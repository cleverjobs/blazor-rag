# tab strip with razor component - calling component's OnInitializedAsync

## Question

**RoyRoy** asked on 27 Sep 2019

I have a tab strip with a razor component (mycontrol.razor) inside the first tab. Inside my component's OnInitializedAsync() I load a Telerik grid with data. If I click on the 2nd tab (or any other one) and then click back to the first tab then my component's OnInitializedAsync() method is called again. Is this supposed to happen? I tried a different vendor's tab and it doesn't do that which I think is correct behaviour. Thanks.

## Answer

**Marin Bratanov** answered on 30 Sep 2019

Hello Roy, This behavior is expected - when switching between tabs we use conditional C# logic to remove the inactive tabs from the DOM. This means that when you return to a tab its components will be initialized anew, as is the Blazor way. For the contents to not re-initialize, the tabs need to only be hidden with CSS instead of conditional statements. The downside of this approach is that it will keep more components in the circuit and in the DOM, and can reduce performance (both on initial load, and while working with the app). It is likely that Syncfusion's components would do that, as they are wrappers over jQuery widgets and not native Blazor components like ours. That said, I have logged such a feature for review, though, and you can Follow its status in this page (I added your vote already): [https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.](https://feedback.telerik.com/blazor/1431932-tabs-can-hide-with-css-only-to-avoid-re-initializing.) In the meantime, you can consider storing the data at the level of the tabstrip (perhaps through an EventCallback from the tab contents) so that you load the data only once, and then receive it as a Parameter in the tab content. Regards, Marin Bratanov
