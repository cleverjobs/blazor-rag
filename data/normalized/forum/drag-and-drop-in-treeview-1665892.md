# Drag and Drop in Treeview

## Question

**Mat** asked on 30 Sep 2024

Hi, I am trying to implement Drag and Drop on the Blazor Treeview component. I am using version 4.4.0 and have been referencing this documentation: [https://docs.telerik.com/blazor-ui/components/treeview/drag-drop#ondragstart-event](https://docs.telerik.com/blazor-ui/components/treeview/drag-drop#ondragstart-event) So far The event "OnDragStart" does not exist, The class "TreeViewDragStartEventArgs" does not exist. Your documentation never seems to list when functionality is available so I have no idea if it is the version I am using, something I have done, or your components. Would love some help clearing this up.

## Answer

**Tsvetomir** answered on 30 Sep 2024

Hello Matthew, Thank you for the provided information. The TreeView drag events were introduced in version 5.0.0. That is the reason why, you are encountering such an error. So to benefit from the component and the desired functionality, I recommend upgrading to at least version 5.0.0. Additionally, our documentation is targeting our latest version, which is 6.2.0. To view the documentation for a specific version, it is required to download it from your Telerik account download section. For example for version 4.4.0 download the following pdf file - " telerik.ui.for.blazor.4.4.0.pdf ". I hope the provided information serves you well. Rest assured, I'm available to provide further assistance and support should you encounter any challenges, even after completing the upgrade. Regards, Tsvetomir Progress Telerik

### Response

**Matthew Bishop** commented on 30 Sep 2024

Hi Tsvetomir, Yeah upgrade is not possible unless you want to credit my account with the latest version? My license is only for version 4.4 or below. As a single dev working on a long term self-funded project there is just not the ability to fork out 2k every year in the hope that we will be purchasing a complete library, rather than a half finished one. Cheers, Matthew
