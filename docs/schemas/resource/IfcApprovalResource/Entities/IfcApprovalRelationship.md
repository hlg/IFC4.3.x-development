# IfcApprovalRelationship

An _IfcApprovalRelationship_ associates approvals (one relating approval and one or more related approvals), each having different status or level as the approval process or the approved objects evolve.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Subtyped from _IfcResourceLevelRelationship_, order of attributes changed.

## Attributes

### RelatingApproval
The approval that other approval is related to.

### RelatedApprovals
The approvals that are related to another (relating) approval.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The cardinality of this attribute has been changed to SET.