# Grid validation

## Question

**TomTom** asked on 08 May 2019

From my initial experiments and looking at the documentation it seems like the TelerikGrid component doesn't currently have features for performing data validation, is that correct? If so, are there plans to add validation for the grid, and if so what sort of timescale are we looking at for those?

## Answer

**Bozhidar** answered on 09 May 2019

Hi, Yes, the built-in validation in the Grid edit forms is on our immediate roadmap, and you should see it available in a few weeks at the most. Regards, Bozhidar

### Response

**Tom** answered on 09 May 2019

Thanks Bozhidar. Is the roadmap something you could share with the community? It would be really useful to know which features are coming and in what sort of timescale, it will help us work out what we can use Telerik components for and what we'll need to develop ourselves? I had a look on GitHub and it doesn't look like the Blazor project is open-source, otherwise I'd track the plans there.

### Response

**Marin Bratanov** answered on 10 May 2019

Hello Tom, We are working on a roadmap page as well, I expect that it will be live in a URL similar to this: [https://www.telerik.com/support/whats-new/blazor-ui/roadmap](https://www.telerik.com/support/whats-new/blazor-ui/roadmap) Things are still quite dynamic, because, while we do have some ideas, we are also trying to follow very closely the feedback we receive, sometimes we even implement features or fixes on the days that we receive requests. For the time being, A good spot to provide feedback and to see what is popular (i.e., is likely to get implemented sooner) is our

### Response

**Ziga HABJAN** answered on 09 Dec 2019

Is the feature ready (grid validation)?

### Response

**Marin Bratanov** answered on 09 Dec 2019

Hi Ziga, The PopUp edit form has an EditForm and supports validation. You can see it in action in this demo: [https://demos.telerik.com/blazor-ui/grid/editing-popup](https://demos.telerik.com/blazor-ui/grid/editing-popup) There is also an example in the documentation: [https://docs.telerik.com/blazor-ui/components/grid/editing/popup](https://docs.telerik.com/blazor-ui/components/grid/editing/popup) Regards, Marin Bratanov

### Response

**laboratorysystemdevelopment** answered on 22 May 2020

Hi Marin! Can you confirm whether the Incell Blazor editting already has a validation feature?

### Response

**Marin Bratanov** answered on 24 May 2020

Hello, InCell editing and InLine editing cannot have an out-of-the-box validation because that's not how validation in Blazor works. You can read more about this here: [https://feedback.telerik.com/blazor/1447439-is-there-a-way-to-implement-custom-validation-in-a-blazor-telerik-grid-when-pressing-save-update-command-button-if-not-is-there-plans-on-providing-custom-validation-as-a-feature-in-the-near-future.](https://feedback.telerik.com/blazor/1447439-is-there-a-way-to-implement-custom-validation-in-a-blazor-telerik-grid-when-pressing-save-update-command-button-if-not-is-there-plans-on-providing-custom-validation-as-a-feature-in-the-near-future.) What you can consider is using the OnUpdate and OnCreate events to determine if the data is valid and if not - show a message to the user and put the item back in edit/insert mode through the grid state: [https://docs.telerik.com/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item.](https://docs.telerik.com/blazor-ui/components/grid/state#initiate-editing-or-inserting-of-an-item.) Regards, Marin Bratanov

### Response

**rad** commented on 31 May 2022

What does the template code look like ? slope unblocked
