# MessageBoxService in Azure

## Question

**Gia** asked on 06 Apr 2020

Hi I'm using your implementation of MessageBoxService in blazor-ui-master. All works fine but........ when I deploy the webapp in Azure happen a strange issue When one client open the messagebox all the other connected user, in different places connected to the same web app, can see the same windows opened. I know: this is a very stupid question, but I do not know how to solve it. I've tried to modify in startup from addscoped to addtransient..... but I obtain the same issue. Tnx

## Answer

**Marin Bratanov** answered on 06 Apr 2020

Hi Giampaolo, The sample in the public repo is not something we made so it is not something we support. That said, this does, indeed, look like a global variable or instance being used so perhaps there is such an issue in the code (say, a static class, or another hidden service that is not scoped but is a singleton). Regards, Marin Bratanov

### Response

**Giampaolo** answered on 06 Apr 2020

Yes tnx for rapid reply The problem is the static definition OnShowMessageBox ! Mine was a stupid question ! Excuse me !

### Response

**Marin Bratanov** answered on 07 Apr 2020

Hello Giampaolo, If the issue is present in the repo sample, we'd appreciate a pull request with the fix, it might help a lot of other people too. Regards, Marin Bratanov
