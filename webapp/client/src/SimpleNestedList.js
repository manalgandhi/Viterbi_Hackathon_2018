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

class SimpleNestedList extends React.Component {
  state = { open: false };

  handleClick = () => {
    this.setState({ open: !this.state.open });
  };

  render() {
    const listItems = this.props.devices.map(device => {
      return (
        <ListItem button onClick={this.handleClick} key={device.name}>
          <ListItemText inset primary={device.name} />
          {this.state.open ? <ExpandLess /> : <ExpandMore />}
        </ListItem>
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
