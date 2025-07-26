# Navigating TelerikWizard and child component loose its data

## Question

**MISMIS** asked on 09 May 2024

I added a TelerikWizard with five WizardSteps on a page. No child components, all code directly inside the different steps. Navigating back and forward between the steps works fine, all steps/controls keeps their user input data/state. After a while I had so much content that I wanted refactor some of the steps into components. I made the first component and added it to one of the steps: <WizardStep ... <Content> <TransferLocationTables @ref="refTransfer" LocationId="@VM.SelectedLocation.Id" /> </Content> ... Now when I navigate to that specific step the component is always "reset" and I have to rearrange the data loaded from the DB again, which kind of defeats the whole idea with those steps and being able to go back and forth between them. When I go one step back I can see in the debugger that the component still got all the internal data. As soon as I go forward to that step everything is empty again. Also noticed the components overriden OnParametersSet and OnInitializedAsync methods are called each time I navigate there so clearly the whole component is "reinitialized" and thus loosing the data. So, is this changed behavior due to that when I had all code in the TelerikWizard everything behaved as a single component and thus all data persisted (didn't really leave it), but when I add child components they will automatically reinitialize everytime their step is rendered? I guess I could persist the individual child components state by saving it to the DB and load it everytime I enter that step again, but I'm hoping there is a simpler soluton that I've overlooked (I'm fairly new with coding Blazor but coded .NET for a long time).

## Answer

**Svetoslav Dimitrov** answered on 14 May 2024

Hi, We have an open feature request for the Persist content feature. I have added your Vote for it and you can click the Follow button to receive email notifications on status updates. In the meantime, your solution idea is the best possible. Regards, Svetoslav Dimitrov Progress Telerik
