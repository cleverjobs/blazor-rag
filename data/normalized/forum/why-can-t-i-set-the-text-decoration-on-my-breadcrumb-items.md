# Why can't I set the text-decoration on my Breadcrumb items?

## Question

**Dav** asked on 14 Apr 2022

Here is my code: <TelerikBreadcrumb Data="@Items" Width="100%" Class="ecsg-breadcrumb"> <SeparatorTemplate> <span class="ecsg-breadcrumb-item"> / </span> </SeparatorTemplate> <ItemTemplate> <div class="ecsg-breadcrumb-item" role="button"> <span> @context.Text </span> </div> </ItemTemplate> </TelerikBreadcrumb> .ecsg-breadcrumb { background-color: #002547!important; color: white;
}.ecsg-breadcrumb-item { color: white; font-size: 1.25rem; text-decoration:none; text-decoration-thickness: 0px;
} Yet here is the result:

## Answer

**Svetoslav Dimitrov** answered on 18 Apr 2022

Hello David, My best suggestion would be to use a more specific CSS selector to target the div with class ecsg-breadcrumb-item. Below, I have added a possible selector: .k-breadcrumb.k-breadcrumb-container.k-breadcrumb-item.ecsg-breadcrumb-item Let me know if this helped you move forward with your application. Regards, Svetoslav Dimitrov
