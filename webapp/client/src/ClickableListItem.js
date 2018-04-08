import React from "react";
import { withStyles } from "material-ui/styles";
import { ListItem, ListItemText, ListItemIcon } from "material-ui/List";
import DevicesIcon from "material-ui-icons/Devices";
import WifiIcon from "material-ui-icons/Wifi";

const styles = theme => ({
  root: {
    backgroundColor: theme.palette.background.paper
  },
  clickable: {
    color: "blue"
  }
});

class ClickableListItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }

  render() {
    const { classes } = this.props;
    return (
      <ListItem
        button
        onClick={() => this.props.handleDeviceClicked(this.props.idx)}
        key={this.props.name}
        className={classes.root}
      >
        <ListItemIcon>
          <DevicesIcon />
        </ListItemIcon>
        <ListItemText
          inset
          primary={this.props.name}
          className={classes.clickable}
        />
        {this.props.idx === this.props.chosenDeviceIdx ? <WifiIcon /> : ""}
      </ListItem>
    );
  }
}

export default withStyles(styles)(ClickableListItem);
