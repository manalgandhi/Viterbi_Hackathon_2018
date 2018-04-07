import React, { Component } from "react";
import CssBaseline from "material-ui/CssBaseline";
import Grid from "material-ui/Grid";
import Paper from "material-ui/Paper";
import Typography from "material-ui/Typography";
import { withStyles } from "material-ui/styles";
import ListItemComposition from "./ListItemComposition";
import SimpleExtentionPanels from "./SimpleExtentionPanels";
import SimpleNestedList from "./SimpleNestedList";
import SwitchListSecondary from "./SwitchListSecondary";

const styles = theme => ({
  app: {
    margin: "3%"
  }
});

class App extends Component {
  render() {
    const { classes } = this.props;
    const devicesPackets = [
      { name: "14:21 04-07 2018", values: ["aaa", "bbbb"] },
      { name: "14:35 04-07 2018", values: ["aaa", "bbbb"] }
    ];
    return (
      <React.Fragment>
        <CssBaseline />
        <div className={classes.app}>
          <header className="App-header">
            <h1 className="App-title">TEAM 1</h1>
          </header>
          <Grid container spacing={16}>
            <Grid item xs={6}>
              <h2>Devices we detect</h2>
              <SimpleNestedList />
            </Grid>
            <Grid item xs={6}>
              <h2>Packets the device sends/receives</h2>
              <SimpleExtentionPanels devicesPackets={devicesPackets} />
            </Grid>
          </Grid>
        </div>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(App);
