# DataBinding broken on inherited classes

## Question

**alm** asked on 12 May 2021

As long as there has been data binding in .Net, you have been able to bind to properties of inherited classes (and it gets resolved at runtime). You have long had an issue that while databinding works on these properties, sorting does not. You're WPF datagrid has this problem (which we asked to get fixed years ago and got an acknowledgement of the problem along with vague promise to fix) and your Blazor datagrid suffered same issue (we are told it was because you were relying on LINQ to do the sorting). One should note that WPF's built in datagrid worked fine binding and sorting these properties. Now, with the latest 2.24 release, you have gone the opposite direction and broke databinding very disappointing to see and makes your product currently unusable.

## Answer

**Svetoslav Dimitrov** answered on 12 May 2021

Hello Eric, I know how frustrating it might be to change to a new version and something that has already been working properly to unexpectedly stop doing so. I would like to confirm that we have not made a change to the way the Grid consumes its data or any data binding mechanism regarding the Grid. More information on what changes we introduced to the Grid or any other component can be found from our release history. Firstly, let me verify that we are on the same page about the use case: The Data parameter of the TelerikGrid is bound to a list of a class that inherits another class. When you try to sort, filter, or group the Grid operations do not seem to work. As an attached file I have added a demo application that showcases a TelerikGrid bound to a model that inherits a base model: public class BasePersonClass { public int PersonalNumber { get; set; } public string FirstName { get; set; } public string LastName { get; set; } public int Age { get; set; }
} public class PersonWorkClass: BasePersonClass { public string CompanyName { get; set; } public string Position { get; set; } public int CompanyId { get; set; }
} The Grid Data parameter is bound to a List of PersonWorkClass: public List<PersonWorkClass> GridData { get; set; } The Grid has the following features that are enabled: Editing - set to Popup mode Sorting Filtering - through the FilterMenu Grouping Can you give the application a run and see if it works as expected for you? If it does, you can compare it against your own and see if any differences cause the issue. If this does not help, can you modify the attached application so that the issue is reproducible? Another step that would help us properly investigate and provide another solution might be for you to give us more details on the collection the Grid is bound to if providing a runnable sample is hard to accomplish due to the complexity of your application. Additional information If you would like to use interfaces and models that are created from service when working with the Grid and you would like to instantiate models in a more complex manner and a parameterless constructor is not enough, you can see the OnNeedModel feature request. This event will fire before the OnEdit, before inserting an item, and before filtering so that you will be able to provide your own model instance. If you would like to see that event implemented you can Vote for it and Follow the thread to receive email notifications on status updates. Regards, Svetoslav Dimitrov

### Response

**almostEric** commented on 12 May 2021

I'll take a look at your project, but this is our use case: public abstract class BasePersonClass { public int PersonalNumber { get; set; } public string FirstName { get; set; } public string LastName { get; set; } public int Age { get; set; } } public class PersonWorkClass : BasePersonClass { public string CompanyName { get; set; } public string Position { get; set; } public int CompanyId { get; set; } } public class ManagerWorkClass : BasePersonClass { //some other properties } public List<BasePersonClass> GridData { get; set; } //Note the list is of the base class, so can contain items of either the two sub classes MARKUP: <TelerikGrid Data=@GridData> <GridColumns> <GridColumn Field="CompanyName" Sortable="true" Title="Company" /> Previously, the company name would display fine (or it would be blank if the object was a ManangerWorkClass), but it would not be sortable. Now, it doesn't even compile, because it says that CompanyName doesn't belong to BasePersonClass. Looks like some late-binding got changed to early binding :/

### Response

**Svetoslav Dimitrov** commented on 17 May 2021

Hello Eric, In a TelerikGrid you should provide a single model. The Grid should not be bound to a base class, because it would populate its data collection with instances of the inherited classes. We have updated the documentation to better explain this situation: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound](https://docs.telerik.com/blazor-ui/components/grid/columns/bound) A way to achieve the desired behavior would be to use the OnRead event: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations](https://docs.telerik.com/blazor-ui/components/grid/manual-operations)

### Response

**almostEric** commented on 17 May 2021

Hi great, you just broke how data binding has worked for over 10 years. As mentioned your product is now unusable. I'll be asking for a refund unless this is fixed

### Response

**almostEric** commented on 17 May 2021

also, your solution leads to completely breaking the MVVM model. The same thing I was forced to do to get sorting working correctly with your WPF grid. Really disappointed with your company right now, and regret renewing my subscription

### Response

**Svetoslav Dimitrov** answered on 19 May 2021

Hello Eric, I am sorry to read that you feel this way about our product. Firstly, let me note that we still do not have the full picture of your use case and implementation. This is really important because we want to help you, but need more details to do so.. You can use the attached application as a base to reproduce the unwanted behavior. A good example would be one that is running as expected for you in a previous version and is broken in 2.24.0. I would also like to confirm that we made no changes to the way the Grid consumes its data so the data binding did not change. Based on your previous messages I would like to address each point you made in its respective turn. As an attached file you can see a simplified version of the demo application I have added in my previous answer and I will use it as the basis of this message. You just broke how data binding worked When I am testing the behavior of the Grid in the attached application I can observe the same behavior both in 2.23.0 and 2.24.0. I would like to offer a quick summary of the steps I have taken and the observed results: Testing steps: The Grid is bound to a collection of the BasePersonClass The component renders as expected, meaning that all columns are populated correctly with data. Try sorting a column that has no data, for example - the CompanyName Observed results: The Grid populates each column with the correct data which means that the data binding works as expected. The Grid throws System.ArgumentException: Invalid property or field - 'CompanyName' for type: BasePersonClass when sorting a column from the PersonWorkClass Reason for the ArgumentException about CompanyName: When you are using the built-in features of the Grid such as Sorting in the background the Grid creates expressions to evaluate the items and sort them. In this case, the type of model bound to the Grid is the BasePersonClass, but when sorting the Grid by CompanyName, which is part of the PersonWorkClass the model passed to the expressions changes, thus the error. One more thing I should point out is that the Grid still sorts as expected when you click on a column which field is part of the BasePersonClass - for example, the PersonalNumber. Sorting a column with no data should not be possible since there would be no sorting condition. The issue you are facing is an unsupported scenario which we should have documented better at an earlier stage. Your solution leads to completely breaking the MVVM model The OnRead event does not break the MVVM pattern. This is a standard Read (C R UD) operation that gives you the ability to customize the built-in features of the Grid such as sorting, filtering, and paging. If this event is not declared explicitly in the markup of the Grid will perform the Read operation internally Conclusion If the project does not reflect the actual situation you are facing, please modify it and send it back to us (might be in a private ticket too) so that we can further investigate the issue. Regards, Svetoslav Dimitrov Progress Telerik
