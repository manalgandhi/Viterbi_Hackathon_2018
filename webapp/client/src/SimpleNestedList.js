import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "material-ui/styles";
import ListSubheader from "material-ui/List/ListSubheader";
import List, { ListItem, ListItemIcon, ListItemText } from "material-ui/List";
import Collapse from "material-ui/transitions/Collapse";
import InboxIcon from "material-ui-icons/MoveToInbox";
import DraftsIcon from "material-ui-icons/Drafts";
import SendIcon from "material-ui-icons/Send";
import ExpandLess from "material-ui-icons/ExpandLess";
import ExpandMore from "material-ui-icons/ExpandMore";
import StarBorder from "material-ui-icons/StarBorder";

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
    const { classes } = this.props;

    return (
      <div>
        <List>
          <ListItem button onClick={this.handleClick} className={classes.root}>
            <ListItemText
              inset
              primary="Apple's multi-purpose item like iPhone"
            />
            {this.state.open ? <ExpandLess /> : <ExpandMore />}
          </ListItem>
          <Collapse in={this.state.open} timeout="auto" unmountOnExit>
            <List component="div" disablePadding>
              <ListItem button className={classes.nested}>
                <ListItemText inset primary="iPhone6 #1" />
              </ListItem>
            </List>
          </Collapse>
        </List>
      </div>
    );
  }
}

export default withStyles(styles)(SimpleNestedList);
