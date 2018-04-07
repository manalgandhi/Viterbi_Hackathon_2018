import React from "react";
import { withStyles } from "material-ui/styles";
import List, { ListItem, ListItemText } from "material-ui/List";
import ExpandMore from "material-ui-icons/ExpandMore";
import ExpandLess from "material-ui-icons/ExpandLess";

const styles = theme => ({
  root: {
    backgroundColor: theme.palette.background.paper
  },
  nested: {
    paddingLeft: theme.spacing.unit * 4
  }
});

class ClickableListItem extends React.Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }

  render() {
    return (
      <ListItem
        button
        onClick={() => this.props.handleDeviceClicked(this.props.idx)}
        key={this.props.name}
      >
        <ListItemText inset primary={this.props.name} />
        {this.props.idx === this.props.chosenDeviceIdx ? (
          <ExpandLess />
        ) : (
          <ExpandMore />
        )}
      </ListItem>
    );
  }
}

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
