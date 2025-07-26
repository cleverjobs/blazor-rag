# Using TelerikForm in Template in TelerikListView

## Question

**Jef** asked on 09 Apr 2021

Hi, I'm wondering if there's any way to implement TelerikForm in the Template in TelerikListView? Here's my code below, I have a TelerikListView and I wish to place TelerikForm in its Template without the columns, I only want the feature of form to submit my delete action, after submitting the form, it'll trigger Delete_Click then call another component Confirm, which is a customized confirmation block to avoid deleting without confirmation. However, the context.UserName always showed the last data of context, I tried several times and found out the TelerikListView looped over without entering TelerikForm, is that a feature of TelerikListView or did I do something wrong? Please help me out, thank you in advance. 01. <TelerikListView Data="@Users" Width="800px" Pageable="true"> 02. <HeaderTemplate> 03. <h2>Users List</h2> 04. </HeaderTemplate> 05. <Template Context="context"> 06. <div class="listview-item"> 07. <h4>User Id: @context.Id</h4> 08. <h4>User Email: @context.Email</h4> 09. </div> 10. <TelerikForm Model="context" OnValidSubmit="Delete_Click"> 11. <FormValidation> 12. <DataAnnotationsValidator></DataAnnotationsValidator> 13. </FormValidation> 14. <FormItems> 15. <FormItem> 16. <Template> 17. </Template> 18. </FormItem> 19. </FormItems> 20. <FormButtons> 21. <TelerikButton class="btn btn-danger" ButtonType="ButtonType.Submit"> 22. Delete 23. </TelerikButton> 24. </FormButtons> 25. </TelerikForm> 26. <Confirm @ref="DeleteConfirmation" ConfirmationChanged="ConfirmationDelete_Click" 27. ConfirmationMessage=@($"Are you sure you want to delete \"{context.UserName}\"?")></Confirm> 28. </Template> 29. </TelerikListView>

## Answer

**Jeff** answered on 09 Apr 2021

Sorry, the problem is the Confirm component instead of the TelerikForm. I put the Confirm inside the Template, but the context.UserName always showed the last data.

### Response

**Marin Bratanov** answered on 09 Apr 2021

Hello Jeff, I am not sure what the <Confirm> component has, but I suggest you simply use the Telerik Confirm dialog: [https://demos.telerik.com/blazor-ui/dialog/predefined-dialogs](https://demos.telerik.com/blazor-ui/dialog/predefined-dialogs) - you can easily integrate it with clicks on buttons and other methods to determine whether to continue code execution based on the user response. I can also suggest you use the built-in listview editing and also step on this example for validation. Of course, using a form in the template is also a valid approach - you can do confirmation on the OnValidSubmit, for example. Regards, Marin Bratanov

### Response

**Jeff** answered on 16 Apr 2021

Thanks for replying, I figured out the problem was I put the Confirm in the list itself instead of creating a component, yet the Confirm should be one by one relationship with each row, so I created a component to place the Confirm and it was solved. I chose the form was because I needed a confirm window to let the user make sure if they really want to delete the data, I didn't see the related function in listview editing, or did I miss it? If there's something I didn't notice please let me know, thank you.

### Response

**Marin Bratanov** answered on 16 Apr 2021

Hello Jeff, At the moment, you can easily achieve this with the Telerik Confirm dialog and the OnClick handler of the built-in Delete button in the listview. You can see a similar example for the grid here, and the same approach would work for the listview. Regards, Marin Bratanov

### Response

**Jeff** answered on 05 May 2021

Thank you Bratanov, this Confirm dialog works well.
