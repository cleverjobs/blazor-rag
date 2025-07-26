# Doesn't work Rebind Method in the Telerik schedule component

## Question

**sud** asked on 30 Oct 2022

I want to refresh the Telerik schedule component. For that, I used this link: [https://docs.telerik.com/blazor-ui/components/scheduler/refresh-data](https://docs.telerik.com/blazor-ui/components/scheduler/refresh-data) But, In my code doesn't work Rebind Method, I want to refresh the Telerik schedule component. For that, I used this link: [https://docs.telerik.com/blazor-ui/components/scheduler/refresh-data](https://docs.telerik.com/blazor-ui/components/scheduler/refresh-data) But, In my code doesn't work Rebind Method, I can see this problem: Then I also try a sample code in the above link in my code (by copying and pasting). doesn't work. It generates the same issues. Please help me!! Thank You.

## Answer

**Nadezhda Tacheva** answered on 01 Nov 2022

Hi Sudath, The Rebind() method of the Scheduler was exposed in UI for Blazor version 3.6.0. In case you are using an older version of the product, the component will not be able to recognize this method. Generally speaking, the documentation is based on the latest version of UI for Blazor. We recommend using the latest product version to have access to the full set of functionalities the components expose. Having the above in mind, you can upgrade the UI for Blazor package your application uses to at least 3.6.0. You may then try invoking the Rebind() method. In case you are experiencing any issues, please send us a runnable reproduction so we can test and verify what is causing them. Thank you in advance! Regards, Nadezhda Tacheva Progress Telerik
