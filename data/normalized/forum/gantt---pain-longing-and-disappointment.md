# Gantt - pain, longing and disappointment

## Question

**Iva** asked on 10 Nov 2021

In my project, the turn has finally come to the implementation of the Gantt diagram. I looked with envy at the component from Syncfusion, but stubbornly did not allow myself to combine components from different developers, I try to be loyal only to Telerik. The long-awaited release of the component and - a huge disappointment! Guys, this is not a product that you are not ashamed to release for release. It's more like "make them at least something to be." Where are the templates for rows, headings? What is this totally inappropriate editing? What the hell is a double click to edit? Where is the managed expand \ collapse? Where is the state management? Where is the slider position management? Do you think it's okay to leave so much blank space where there are no tasks in the "year" view? Specifying the "RangeStart" property for the GanttYearView does not affect the display in any way - all the months of the year will still be displayed. You didn't even bother to include a description of properties for localization! Take the Syncfusion component as a reference and do it with all your heart as you can, like your Grid. So far - a complete failure.

## Answer

**Maria Ivanova** answered on 15 Nov 2021

Hi Ivan, My name is Maria Veledinova and I am the Product Manager for Telerik UI for Blazor. I am sorry to hear that the Gantt component has caused disappointment and does not meet your requirements. Based on your feedback we revised our planning and we will deliver a Gantt focused release in February. As we understand the importance of the Gantt features you listed, we would like to discuss further with you their priorities in a support ticket or online conversation. During our meeting we would like to talk over your feedback and in collaboration with you, to see if we can we can address some of them even earlier. Let me know if this proposal sounds good and I will follow-up with arranging the next steps. Kind regards, Maria Veledinova

### Response

**Ivan** commented on 15 Nov 2021

This is exactly what I like about Telerik - readiness for discussion and attention to customers. Unfortunately, I cannot cope with a live dialogue in English, but I will try to formulate the requirements for the component in writing. The component is extremely important and its quality will noticeably affect the attractiveness of Telerik components in general, since in fact there is currently only one alternative from Syncfusion. How do I indicate the desired requirements for a component?

### Response

**Maria Ivanova** answered on 15 Nov 2021

Hi Ivan, Putting down the requirements in writing with assigned priority would be great! You can use P1, P2, P3 or other priority scale that is convenient for you. I would suggest we bring this conversation to our support ticket system. Once you submit the requested features along with their priority, we would be able to review them with the team and come back with estimated time of delivery. Thank you! Maria Veledinova PM @

### Response

**Ivan** commented on 15 Nov 2021

Done, added feature requests for the component. Make it great! I suppose that the activity of supporting the votes will not be high, but I expect your actions anyway.

### Response

**Maria Ivanova** commented on 17 Nov 2021

Hi Ivan, Thank you for the valuable feedback and willingness to collaborate! As we took the conversation over email, I just wanted to thank you for taking the time to work with us on this and make the component better and more powerful. We hope that the updates to the release plan for the Gantt will make developing apps with it a pleasure for everyone. Kind Regards, Maria Veledinova PM @Progress Telerik

### Response

**Ivan** answered on 02 Dec 2021

While we are waiting for the component to be updated, please tell me - is there a way to display all tasks minimized by default? I need to display a large list of tasks, each with a rich tree of nested tasks. As a result, the component works very slowly. And if all tasks are minimized by default, everything is ok. This update will be enough for the first time to start using the component. I tried to do this: For the parent task, the property HasChildren=false is set by default Next, I create a command column <GanttCommandColumn Locked="true" Context="context" Width="3.5em"> @if (!(context as TaskData).ParentId.HasValue)
{ <TelerikButton Title="Show tasks" OnClick="@(()=> ShowChildren(context as TaskData))"> <div class="row"> <div class="col d-flex px-2 justify-content-center"> <i class="fas fa-edit" /> </div> </div> </TelerikButton> } </GanttCommandColumn> @code {
private async void ShowChildren(TaskData args) {
args.HasChildren=true;
await InvokeAsync(StateHasChanged);
}
} But it doesn't work as expected. The parent task's expand icon does not appear, the component does not redraw

### Response

**Dimo** commented on 07 Dec 2021

Hi Ivan, I made some experiments and the easiest way to render collapsed tasks is - set HasChildren to false for all root tasks set HasChildren to the actual value in OnAfterRenderAsync This approach will spare the need for custom buttons, which also don't expand the tasks (I am waiting for some additional dev input here). Here is a runnable REPL test page.

### Response

**Ivan** commented on 07 Dec 2021

Thank you very much, dear friend! It worked, even for nested tasks.
