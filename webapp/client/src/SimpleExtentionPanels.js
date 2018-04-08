import React from "react";
import ExpansionPanel, {
  ExpansionPanelSummary,
  ExpansionPanelDetails
} from "material-ui/ExpansionPanel";
import { withStyles } from "material-ui/styles";
import Typography from "material-ui/Typography";
import ExpandMoreIcon from "material-ui-icons/ExpandMore";
import SimpleTable from "./SimpleTable";

const styles = theme => ({
  root: {
    flexGrow: 1
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: "33.33%",
    flexShrink: 0
  },
  secondaryHeading: {
    fontSize: theme.typography.pxToRem(15),
    color: theme.palette.text.secondary
  }
});

function SimpleExpansionPanels(props) {
  const { classes } = props;

  const panelItems = props.packets.map(packet => (
    <ExpansionPanel key={packet.time + packet.date}>
      <ExpansionPanelSummary expandIcon={<ExpandMoreIcon />}>
        <Typography className={classes.heading}>
          {packet.time + " " + packet.date}
        </Typography>
        <Typography className={classes.secondaryHeading}>
          {packet.is_allowed === "1" ? "" : "Not allowed(Blocked)"}
        </Typography>
      </ExpansionPanelSummary>
      <ExpansionPanelDetails>
        <SimpleTable packet={packet} />
      </ExpansionPanelDetails>
    </ExpansionPanel>
  ));
  return <div>{panelItems}</div>;
}

export default withStyles(styles)(SimpleExpansionPanels);
