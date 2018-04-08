import React from "react";
import ClickableListItem from "./ClickableListItem";
import { withStyles } from "material-ui/styles";
import List from "material-ui/List";

const styles = theme => ({
  root: {
    backgroundColor: theme.palette.background.paper
  },
  nested: {
    paddingLeft: theme.spacing.unit * 4
  }
});

class SimpleNestedList extends React.Component {
  state = { open: false };

  render() {
    const listItems = this.props.devices.map((device, idx) => {
      return (
        <ClickableListItem
          key={device.name}
          name={device.name}
          idx={idx}
          chosenDeviceIdx={this.props.chosenDeviceIdx}
          handleDeviceClicked={this.props.handleDeviceClicked}
        />
      );
    });

    return (
      <div>
        <List>{listItems}</List>
      </div>
    );
  }
}

export default withStyles(styles)(SimpleNestedList);
