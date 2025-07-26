# Hierarchical Drawer and MainNavLayout

## Question

**Wil** asked on 23 Jul 2020

I have implemented the drawer following your sample to use the drawer as navigation in the main site layout. I have also used the template to create hierarchical menu. I believe since I am using the template, the @Body will not be set for the url content? Do you have a sample which uses hierarchical template and is able to navigate to a Razor Component. I have tried using a RenderFragment on each drawer item and bind that value in the content field. It seems to be rather slow. Also, when I render the component this way it seems any layout template I have specified at the component level is ignored. Do you have any suggestions? Thank you in advance.

## Answer

**Svetoslav Dimitrov** answered on 23 Jul 2020

Hello Will, The Template takes away all built-in functionalities of the Drawer including the navigation. You can use the @onclick event on the HTML element containing your item to invoke a method with NavigationManager that redirects the user to a desired URL. This is not only restricted to the NavigationManager as it can be an <a>, <NavLink> etc. As attached file I am sending a project where such implementation is done. I have updated our documentation regarding the Template, you can see it from this link. Regards, Svetoslav Dimitrov

### Response

**Will** answered on 23 Jul 2020

Thank you, Svetoslav. It worked perfectly.
