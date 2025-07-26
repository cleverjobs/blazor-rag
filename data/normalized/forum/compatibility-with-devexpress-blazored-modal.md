# Compatibility with Devexpress & Blazored Modal

## Question

**Mat** asked on 24 Jun 2021

Hello, I want to use your TelerikEditor in my existing project. Our project primarily uses DevExpress along with a few other components like Blazored Modal. First I want to know if there are any known issues mixing Devexpress and Telerik in the same project? My main concern is having CSS clashes between the two libraries. 2nd, we use Blazored Modal which has a cascading parameter (CascadingBlazoredModal) that wraps the router. When I try to show the TelerikEditor in a modal I get the following: " A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration) " I suspect this is because dialog is parented outside of the MainLayout which uses the TelerikLayout. Is it technically feasible to use the TelerikLayout inside a view? Thanks, Matt B.

## Answer

**Marin Bratanov** answered on 26 Jun 2021

Hi Matt, To each question in turn: Compatibility with DevExpress - we do try to encapsulate our own styling inside our own classes and selectors, so we should not generally affect other components and parts of your page. That said, we do not test or support compatibility with such third party components and we cannot guarantee they will not bring in something that can break our components. BlazoredModal - you are correct, their root component puts things outside of our root component and you get that issue. I'd suggest using the Telerik Window for your popup container instead. Regards, Marin Bratanov

### Response

**Matt** commented on 28 Jun 2021

Thanks for your feedback. Unfortunately the Telerik Window does not meet our requirements.

### Response

**Marin Bratanov** commented on 29 Jun 2021

Could you provide some more details on what you find lacking? Also, this sample help: [https://github.com/telerik/blazor-ui/tree/master/common/message-box](https://github.com/telerik/blazor-ui/tree/master/common/message-box)
