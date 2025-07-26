# Page is not re-rendering after URL parameter changed

## Question

**con** asked on 17 Jun 2020

Hi, I'm using "nav-link" to go to page: @page "/orders" I'm also using Parameter which tells me what type of order to be loaded with that Page: @page "/orders/{ord}" There is "nav-item" dropdown on NavMenu.razor page to navigate to Page: <a class="dropdown-item" href="orders/SO">SO</a> <a class="dropdown-item" href="orders/PO">PO</a> The issue is, when I click on any of those links first time (say href="orders/SO") - the Page loads correctly. But then, when I click on href="orders/PO" - the page isn't rendering accordingly even though Parameter on Url has changed. This happens after I replaced JS Table I used before with Telerik Grid. Please advise

## Answer

**Marin Bratanov** answered on 17 Jun 2020

Hello, I am attaching a sample I made for you that shows how you can use the OnParametersSet event to capture parameter change (inlcuding one coming from route parameters). It has a grid whose data changes to reflect the router parameter. If this does not help you solve this, please modify it to showcase the Telerik issue you're facing so I can have a look. Regards, Marin Bratanov

### Response

**const** answered on 17 Jun 2020

Looks like solution you are offering works for me (will test it more intensively later). May I know what's causing the issue? Even this doesn't work: protected override async Task OnParametersSetAsync() { StateHasChanged(); } Please advise.

### Response

**Marin Bratanov** answered on 18 Jun 2020

Hi, What happens would heavily depend on the code you have, but if the parameters change and other parts of the view update, perhaps the issue is with the grid's Data reference - it would ether have to be an ObservableCollection where you can add/remove/clear, or you need a new reference, see the following article for more details and examples: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-force-refresh](https://docs.telerik.com/blazor-ui/knowledge-base/grid-force-refresh) Regards, Marin Bratanov

### Response

**const** answered on 18 Jun 2020

Just FYI. This issue is rather Telerik.Blazor than Telerik.Blazor.Grid one, I think. I have another page where I had exactly the same issue with DatePicker (DP). Until I used JS DP - the routing with parameter worked fine. But once I replaced JS DP with Telerik one - the issue appeared. Your suggestion to use OnParameterChange event instead OnInitializedAsync one bypassing the issue but not resolving one. Looks like Blazor knows that parameter was changed (otherwise OnParameterChange wouldn't work) but something stops or interferes him fire OnInitializedAsync to render the Page. Thoughts?

### Response

**Marin Bratanov** answered on 18 Jun 2020

My though is that whatever JS widget you had did always re-initialize (e.g., by hooking to OnParametersSet or OnAfterRender) which is not a good practice. In a real Blazor component, the field references are more important and they may need to change for a UI update to trigger. At this point I'm still guessing because I have not seen the code that causes a problem with the Telerik components and the approach I showed with the grid is a valid one - navigating between the same component with different route parameter may not re-initialize it, so its OnInitialized event may not fire, but OnParametersSet will. So, if you see a Telerik issue, please open a ticket or post here the minimum viable reproducible (e.g. ,based on my sample) so I can have a look. Regards, Marin Bratanov

### Response

**const** answered on 18 Jun 2020

Ok, Martin, I'll create simple demo project and provide you with one. Thank you for discussion

### Response

**const** answered on 18 Jun 2020

sorry, Marin, not Martin of course, my bad...

### Response

**Marin Bratanov** answered on 18 Jun 2020

No worries, everyone gets my name as Martin with a "t" :) I'll be looking forward to your findings. Perhaps there is a bug, and if so - I want to find it so we can have the chance to fix it. Regards, Marin Bratanov

### Response

**const** answered on 18 Jun 2020

Great, sound like a plan!
