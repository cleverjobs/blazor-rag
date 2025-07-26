# DropDownList Value not Setting in TelerikForm

## Question

**Eve** asked on 25 Jun 2021

I am trying to implement a Popup TelerikForm that has a DropDownList of custom class objects. I can not for the life of me figure out why the values are not setting. If I click on a value in the dropdownlist, it defaults back to the first value. I recreated the error in a very simple demo. I want to create a User object, and the User object has a parameter of Position. The DropDownList should show a list of positions, which it does correctly, but the User should be able to click a position and it Bind to User.Position, which is where my problem is. If a position is clicked in the DropDownList, nothing happens. EDIT: The PopupLayout class is based heavily on the Telerik class. Removing the inheritance does not solve the problem. Changed HandleOnChange to actually update, I took the screenshots while troubleshooting. Even when HandleOnChange only printed the Position to the console, it never did. It seems that the Change event isn't even firing when the DropdownList is in a TelerikForm. Even using @bind-Value does not work.

### Response

**Marin Bratanov** commented on 26 Jun 2021

Could you edit your post to include a text-based version of the problematic code of the Telerik components? We can't run screenshots, and I also see that there is a PopupLayout component that is not a Telerik one and it might be causing issues. In the meantime, you can take a look at this set of articles that describe similar behaviors of popups and they might be useful (the first three are relevant): [https://docs.telerik.com/blazor-ui/components/window/overview#important-notes.](https://docs.telerik.com/blazor-ui/components/window/overview#important-notes.)

### Response

**Marin Bratanov** commented on 26 Jun 2021

Also, can you confirm that the real code you have in your project actually sets the value in the ValueChanged handler? That's mandatory when you don't use two-way binding (see more here and examples here ).

## Answer

**Marin Bratanov** answered on 29 Jun 2021

Hello Everett, I am attaching here a sample that compiles and updates the main model as expected. I hope comparing against it and going through the resources I will link below will help you implement this scenario in your real project. Here are the changes I made based off the latest code snippets: I replaced the custom popup with a Telerik Window. I bound the dropdownlist to a supported value and fixed its event handler type. See more in this article: [https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind.](https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind.) A few notes on what this article shows that pertains to this case: The way the component is bound to a model, the original snippet does not fulfil that What to do when a Value is not provided (the caveat to this is that you won't see the initial value) I got the full model as explained here which can give you a few ideas: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) As a next step I can suggest you consider using an identifier in the user model to act as a foreign key so that you can easily use two-way binding to both show the initial value and to make the rest of the code simpler. Regards, Marin Bratanov

### Response

**Everett** commented on 29 Jun 2021

Thank you so much for the help!
