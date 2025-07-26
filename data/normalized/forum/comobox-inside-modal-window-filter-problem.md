# Comobox inside Modal Window Filter Problem

## Question

**BobBob** asked on 12 Apr 2021

When I try to use the filtering on a combox box that is inside of a Modal Window, the drop down opens behind the modal window and is un-usable? I have attached a screen shot of what is happening? Can this not be used inside a modal window?

## Answer

**Marin Bratanov** answered on 12 Apr 2021

Hi Bob, We are aware of this issue, it is caused by a new Window feature. You can track it here - it will be fixed in our next release (2.24.0) and you can use the workaround from the portal page for the time being: <style>.k-animation-container { z-index: 15000;
}
</style> Regards, Marin Bratanov Progress Telerik
