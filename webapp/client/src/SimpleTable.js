import React from "react";
import { withStyles } from "material-ui/styles";
import Table, { TableBody, TableCell, TableRow } from "material-ui/Table";

const styles = theme => ({});

function SimpleTable(props) {
  return (
    <Table>
      <TableBody>
        <TableRow>
          <TableCell>Source MAC</TableCell>
          <TableCell numeric>{props.packet.src_mac}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Source IP</TableCell>
          <TableCell numeric>{props.packet.src_ip}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Source Port</TableCell>
          <TableCell numeric>{props.packet.src_port}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Destination MAC</TableCell>
          <TableCell numeric>{props.packet.dest_mac}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Destination IP</TableCell>
          <TableCell numeric>{props.packet.dest_ip}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Destination Port</TableCell>
          <TableCell numeric>{props.packet.dest_port}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Is Good</TableCell>
          <TableCell numeric>{props.packet.is_good}</TableCell>
        </TableRow>

        <TableRow>
          <TableCell>Is Allowed</TableCell>
          <TableCell numeric>{props.packet.is_allowed}</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  );
}

export default withStyles(styles)(SimpleTable);
