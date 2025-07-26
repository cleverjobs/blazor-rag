# Wrapping A Card Click

## Question

**Tim** asked on 03 Jun 2021

We're trying to wrap the Telerik card component into my own card deck and card components. I have the following classes that I would like to create in a collection on the page and then have the click events from the button wired up to methods on the page similar to this example. CardDeck - This holds a List of CardItems Card - Contains an individual CardItem object CardItem - Properties of the card as well as a CardButton collection CardButton - Properties of the button as well as a property that represents the method I'd like to wire up on the page. Card.razor iterates through the CardButton collection and creates a TelerikButton object for each item. This is where I'd like to have the CardButton.OnClick wired up. This works fine if I have a method defined in card.razor, but if I try and define a method on the page I can't seem to wire it up (see the example).

## Answer

**Nadezhda Tacheva** answered on 07 Jun 2021

Hi Timothy, If you have a collection of Cards that you want to display in a deck container you can also try this approach - create the container and add the desired styles. In this container you can foreach through the collection and render separate Card component for each of the items in the collection by specifying the desired Card structure and appearance. An example of such a configuration you can find in this demo - Data Cards. It demonstrates how to display a collection of Card items and organize them in a deck layout. You can also check the Card - Layouts demo that showcases how the layout of the collection can be easily modified through built-in classes that the Telerik Themes provide. The attached example demonstrates the described approach, using the data provided in your sample project. To add the events for the corresponding buttons, you can use an instance of EventCallbackFactory and its Create method which serves to create an EventCallback for the provided receiver and callback. In the example I have created two simple methods for the buttons of the first Card to better illustrate how to achieve the desired behavior. I hope you will find the above information useful. If any further question appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva
