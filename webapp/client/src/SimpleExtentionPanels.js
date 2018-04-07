import React from "react";
import ExpansionPanel, {
  ExpansionPanelSummary,
  ExpansionPanelDetails
} from "material-ui/ExpansionPanel";
import Switch from "material-ui/Switch";
import { FormControlLabel, FormGroup } from "material-ui/Form";

import ExpandMoreIcon from "material-ui-icons/ExpandMore";
import SimpleTable from "./SimpleTable";

function SimpleExpansionPanels(props) {
  const devicesPackets = props ? props.devicesPackets : [];
  const panelItems = devicesPackets.map(dp => (
    <ExpansionPanel key={dp.name}>
      <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
        {dp.name}
      </ExpansionPanelSummary>
      <ExpansionPanelDetails>
        <div>
          <SimpleTable />
          <FormGroup row>
            <FormControlLabel
              control={<Switch value="allow" />}
              label="Allow sending/receiving this kind of packets?"
            />
          </FormGroup>
        </div>
      </ExpansionPanelDetails>
    </ExpansionPanel>
  ));
  return <div>{panelItems}</div>;
}

export default SimpleExpansionPanels;
