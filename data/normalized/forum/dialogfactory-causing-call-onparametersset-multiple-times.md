# DialogFactory causing call OnParametersSet multiple times

## Question

**Mic** asked on 11 May 2021

Hello, how to prevent calling "OnParametersSet " multiple times when DialogFactory is used? [CascadingParameter] public DialogFactory Dialogs { get; set; } its firing 2-6 times per page opening. Without DialogFactory, its correct, only 1x. Blazor server app. With PreRendering disabled. Thanks

### Response

**Matthias** commented on 12 May 2021

I use a workaround for this behavior: public override async Task SetParametersAsync(ParameterView parameters) { if (parameters.TryGetValue<int>(nameof(paramName), out var value)) { ... and can stop reloading the component in OnParametersSet Maybe it helps you Regards

### Response

**Nadezhda Tacheva** commented on 14 May 2021

Hi Michal, I tested the firing of the OnParametersSet when using DialogFactory with the following setup - [https://gist.github.com/ntacheva/72a7771ebccd184967e6503902b911ab.](https://gist.github.com/ntacheva/72a7771ebccd184967e6503902b911ab.) It looks to me it fires only twice as expected (I tried with both approaches - with and without DialogFactory and still getting the same result - OnParametersSet fired twice). Could you please test the gist setup as well and let me know if you are experiencing the expected behavior? As a next step, could you send us a reproduction of the behavior you are getting (OnParametersSet firing more than twice), so we can isolate the scenario in which this happens and investigate further? In the meantime, you may also try the the workaround Matthias suggested and see if it will work for your case. Regards, Nadezhda Tacheva

### Response

**Matthias** commented on 14 May 2021

This happens only, If you have the dialog in a child-component (a view for example). The only problem: if you load for example data in OnInitializedAsync the data will be loaded more than once. That’s why I use the workaround- just to compare the parameter-values and to decide, if new data has to be loaded

### Response

**Michal** commented on 14 May 2021

Iam already using the workaround(as the Matthias suggested), but it has also little(but noticable delay) performance impact. Its firing also on EVERY click/action on the existing page(on tabstrip, button, grid). For example when you click button, it fires 3 times. When i remove "public DialogFactory Dialogs", doesnt happening. What will happend when the nesting with DialogFactory occours...cant imagine :) Here is the base setup: 1) MainLayout: @layout TelerikLayout @inherits LayoutComponentBase <AuthorizeView> <Authorized> .... <CascadingValue Value="@Notification" IsFixed="true"> @Body </CascadingValue> </Authorized> </NotAuthorized> </AuthorizeView> 2) page: @page "/account/UserEdit/{userid}" @using Telerik.Blazor; @using Telerik.Blazor.Components; On the page is few more Telerik components. <i class="fas fa-pen" @onclick="@(()=> { PickVisible=true; } )">Pick window</i> <TelerikForm .../> <TelerikWindow Modal="true" @bind-Visible="@PickVisible" ..../> <TelerikTabStrip @bind-ActiveTabIndex="@ActiveTabIndex" Class="col-md-10" .... <TelerikGrid Data="@UserRoles" .../> </TelerikTabStrip> @code { [Parameter] public string userid { get; set; } [CascadingParameter] public DialogFactory Dialogs { get; set; } protected override void OnParametersSet() { --!!Workaround comparing, if values are loaded ONLY FIRST/changed time if (EUser.Id==null || EUser.Id !=userid) { base.OnParametersSet(); //if(IsFirstLoad) LoadBaseData(); } } }

## Answer

**Nadezhda Tacheva** answered on 19 May 2021

Hi Michal, Generally speaking, when using DialogFactory it is expected OnParametersSet to be called twice as we are adding another parameter. However, we managed to reproduce a behavior of OnParametersSet firing six times on initial rendering which does seem not expected. It appears to be observed not only when DialogFactory is used in a child component, but when you use it directly in the parent as well. We will further investigate into this to verify if we can prevent such scenario. For that purpose I have logged a bug report in our public feedback portal to plan and track the case. You can find the public item here - DialogFactory causes more than expected OnParametersSet calls. I have added your vote and since I created the bug report on your behalf, you are subscribed to receive email notifications when its status changes. Matthias, I added your vote as well to keep proper track of the requests for that case. You may also follow it to receive email notifications. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Neil N** commented on 06 Jun 2021

There's more happening here than using DialogFactory on both a parent and child component. I have a child component that uses it but the parent component doesn't. When the page loads OnParametersSetAsync in the child component gets called once, then everything but the child component gets rendered, then OnParametersSetAsync gets called in an infinite loop. Wrapping the OnParametersSetAsync code in an if block stops the loop but that introduces other complications for our code.

### Response

**Nadezhda Tacheva** commented on 09 Jun 2021

Hi Neil N, Could you please send us a runnable reproduction of the described behavior, so we can include this scenario in the investigation as well? Thank you in advance!
