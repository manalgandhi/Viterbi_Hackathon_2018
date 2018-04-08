import React, { Component } from "react";
import axios from "axios";
import CssBaseline from "material-ui/CssBaseline";
import Grid from "material-ui/Grid";
import Button from "material-ui/Button";
import { withStyles } from "material-ui/styles";
import SimpleExtentionPanels from "./SimpleExtentionPanels";
import SimpleNestedList from "./SimpleNestedList";

const styles = theme => ({
  app: {
    margin: "3%"
  }
});

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      devices: [],
      chosenDeviceIdx: -1
    };
    this.fetchDevices = this.fetchDevices.bind(this);
    this.handleDeviceClicked = this.handleDeviceClicked.bind(this);
  }

  handleDeviceClicked(idx) {
    this.setState({ chosenDeviceIdx: idx });
  }

  fetchDevices() {
    const that = this;
    axios({
      method: "get",
      url: "http://127.0.0.1:8080/devices",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    })
      .then(function(response) {
        // console.log(response.data.devices);
        that.setState({ devices: response.data.devices });
      })
      .catch(function(error) {
        console.log(error);
      });
  }

  chosenDeviceName() {
    if (this.state.chosenDeviceIdx === -1) {
      return "";
    }
    return this.state.devices[this.state.chosenDeviceIdx].name;
  }

  render() {
    const { classes } = this.props;
    return (
      <React.Fragment>
        <CssBaseline />
        <div className={classes.app}>
          <header className="App-header">
            <h1 className="App-title">TEAM 1</h1>
          </header>
          <Grid container spacing={16}>
            <Grid item xs={6}>
              <Button
                onClick={this.fetchDevices}
                variant="raised"
                color="primary"
              >
                Fetch devices
              </Button>
              <h2>Devices we detected</h2>
              <SimpleNestedList
                devices={this.state.devices}
                chosenDeviceIdx={this.state.chosenDeviceIdx}
                handleDeviceClicked={this.handleDeviceClicked}
              />
            </Grid>
            <Grid item xs={6}>
              <h2>
                Packets
                {this.state.chosenDeviceIdx === -1
                  ? " the chosen device "
                  : " " + this.chosenDeviceName() + " "}
                sent/received
              </h2>
              <SimpleExtentionPanels
                packets={
                  this.state.chosenDeviceIdx === -1
                    ? []
                    : this.state.devices[this.state.chosenDeviceIdx].packets
                }
              />
            </Grid>
          </Grid>
        </div>
      </React.Fragment>
    );
  }
}

export default withStyles(styles)(App);
