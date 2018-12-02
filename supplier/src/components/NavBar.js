import React, { Component } from 'react'
import { Row, Col, Button, Label} from 'react-bootstrap'

export default class NavBar extends Component {
	render() {
		const { onAddClick } = this.props
		const style = {
			paddingTop: '20px',
			paddingBottom: '20px',
		}
		return (
				<Row className="show-grid" style={style}>
					<Col md={6}>
						<Label>Inventory Management System - Supplier</Label>
					</Col>
					<Col md={6}>
						<Button bsStyle="primary" className="pull-right" onClick={() => onAddClick()}>New Record</Button>
					</Col>
				</Row>
		)
	}
}