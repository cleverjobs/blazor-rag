# Tile component is navigable even though it shouldn't be?

## Question

**JJ** asked on 07 Nov 2024

I am using the teleriktilelayout component. I have resizing and reordering turned off, but we may have it as a feature in the future. Since they are turned off, I need the tiles to be taken out of the tab order and not be navigable. I know that navigable=false is the default, but all the tiles have tabindex=0 (making them tabbable/navigable). Adding navigable=false to the main component doesn't work (and again, it's supposed to be the default). How do I change it to tabindex=-1 on the tiles? Is there any other way to remove the tiles from the tab order? Is this a known accessibility issue?

## Answer

**Dimo** answered on 12 Nov 2024

Hello J, Indeed, this is a bug. I am logging it on your behalf and awarding you some Telerik points. Fortunately, there is an easy JavaScript-based workaround. We are very close to our release this week, but I hope we will manage to squeeze the fix. Regards, Dimo Progress Telerik

### Response

**J** commented on 12 Nov 2024

So I don't want to remove tabindex entirely. I want to change it to tabindex=-1. Tabindex is still a valuable tool for keyboard users. "-1" is used to indicate a non-interactive element. If tabindex is removed, it defaults to the native determination by the element. Testing would be needed to see if removing tabindex from the tiles would indeed make them non-navigable. Tabindex=-1 is a surefire way to make sure they are not navigable.

### Response

**Dimo** commented on 12 Nov 2024

Yes, this is how we fixed it - with tabindex="-1"
