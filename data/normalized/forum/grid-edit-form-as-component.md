# Grid edit form as component

## Question

**Djo** asked on 13 Dec 2023

i would like to make separate control telerik form to update the grid. How to associate this new control with a grid? regards, Djole

## Answer

**Dimo** answered on 15 Dec 2023

Hi Djole, You have two options: Use the built-in Grid edit command and the built-in Grid popup edit container. In this case, see Grid popup form template. Use a completely custom approach that does not use anything built-in from the Grid. In this case, see Grid editing in a custom form. You can still render the custom form in a Window if you like. As you see, in both cases you won't be using the built-in Grid events like OnCreate and OnUpdate. Regards, Dimo Progress Telerik

### Response

**Djordje** answered on 15 Dec 2023

Found an example at [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form) It
is very outdated from the year 2020 built with Telerik 3.x. Many of the
features are now different and need a lot of polish, even though I did
not make it work. Documentation on site is less than sufficient so it
looks that this very needed option for any data processing application
is pretty neglected.

### Response

**Dimo** commented on 15 Dec 2023

The mentioned app requires three things to run with a newer .NET version and the latest Telerik components: Rename GridToolBar to GridToolBarTemplate Migrate a few string icons to SVG or FontIcons Add https in Properties/launchSettings.json We have literally thousands of runnable samples in our demos, documentation, knowledge base, and GitHub blazor-ui repo. The examples in GitHub have lower priority in terms of maintenance, except the sample apps that we showcase on the Demos home page with thumbnails. I understand that an outdated example may look bad, but the primary value of the GitHub apps is to show an idea for achieving a custom scenario. At the same time, we acknowledge that the outdated samples pose a maintenance burden and inconvenience for the customers, so we recently started migrating them to the Knowledge Base. In addition, the Custom Popup Form sample in GitHub is practically the same as the Grid Editing in a Custom Form online demo, with the addition of a Window. The GitHub sample was created before a Grid popup form template existed. The latter is our primary recommendation for your requirement (unless there is a specific reason not to use this approach). Finally, if you have specific feedback or suggestions for the content on our documentation site, do let us know.

### Response

**Djordje** answered on 15 Dec 2023

Dimo, thank you for your early reply. I have to be completely honest. I have been programming for 30+ years, my first programming language was C. I have been in this business for a long time and run a small but relatively successful company that decided this summer to change its development environment. For several reasons, the choice is Blazor and .NET. My task is to test the existing, available tools and to make a choice with which the company will be guided in the following projects. I tested Syncfusion first, and the tool turned out to be very usable. Considering that during the free and unlimited evaluation of the Syncfusion library I also had to adapt to Blazor (before that we hardly used C#), it took a little more time. We were turned away from this by the very high price with a lot of unnecessary features in case we go beyond the limits they have listed for free use. Another tool that I not only evaluated but also bought was Radzen Blazor Studio. A very interesting tool that tries to provide some sort of RAD environment. Considering that before that we used a very powerful but unfortunately outdated tool "Clarion", it can be said that they are still far from full capacity, but the thing still works. And this library can get a very high usability rating and is free in itself. Then, I looked for something even better According to comments on the Internet, your library is at the very top in terms of the number of users. It seems very polished and I have known the company for more than a decade. That's why I tried using your trial library first. Probably due to my clumsiness and your complicated way of accessing the library, I didn't manage to test it, but guided by sound logic, I thought, if it was possible with Syncfusion and Radzen, then it's certainly not a problem with the Telerik library either, so we bought license. That's where I made a mistake. I just don't see how I can separate the table component from the form component. And unfortunately I have to admit that at this moment Radzen is winning by a large margin. Not as full of features as Telerik is but it works with no flows. Telerik is a bit outdated as I wrote in the previous message, neglected. As I receive mail with notification that currently your development is on hold and you are asking for more information, this text is all about that. So, as I understand this business, first it is easy to use, second is reliable functionality, third fast in execution and lastly good design. There is a lot more to say but for now it is enough.

### Response

**Dimo** commented on 18 Dec 2023

Thanks for the detailed insights, Djordje, I appreciate it. Based on...>> I just don't see how I can separate the table component from the form component ... I wonder if there is any misunderstanding between us. The previously provided examples should show exactly that. So, can you please explain what exactly are you trying to do and how the following examples don't fit your purpose? Use separate Grid and Form components for editing Grid items. Use the built-in Grid popup with a manually configured Form component inside. Use a separate Grid, Window and Form for a more detached approach.

### Response

**Djordje** commented on 18 Dec 2023

Simply Dimo, I made all changes in the example previously mentioned
and it works but not the page with this crucial example for me. So no
matter what I tried I did not succeed to activate this option. If it works as you stated then your documentation is no good or I am not capable of understanding it.

### Response

**Dimo** commented on 18 Dec 2023

@Djordje - if possible, please send me a runnable page or a simple app that shows what you have tried, together with an outline what is not working as expected. I will readily see what's going on.

### Response

**Djordje** answered on 19 Dec 2023

Dimo I am sending you Telerik's example of custom popup form. I managed to make it work in .NET 8 but the custom popup form does not show the popup form. Another grid with default pop works with no issue. I remove the bin and obj folder from .zip to avoid antivirus problems.

### Response

**Dimo** commented on 20 Dec 2023

Hi Djordje, It looks like you want to use .NET 8. Migration from older .NET versions to 8 requires some steps, and one of the important ones is interactivity. If user actions on a given page have no effect, then chances are that interactivity is not enabled. This applies to all Razor components in general. I am sending an attached .NET 8 app, which works as expected.

### Response

**ma** commented on 20 Dec 2023

Indid it works. You made substantial changes and now it works. Thank you Dimo for your commitment to solve problems. Djordje
