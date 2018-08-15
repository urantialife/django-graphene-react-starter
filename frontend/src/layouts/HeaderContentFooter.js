import React, { Component } from 'react';
import { Layout, Menu } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;
class HeaderContentFooter extends Component {
  render() {
    return (
      <Layout>
        <Header>
            <Menu
                mode="horizontal"
                theme="dark"
                defaultSelectedKeys={['2']}
                style={{lineHeight: '64px'}}
            >
                <Menu.Item key="1">MyAppName</Menu.Item>
                <Menu.Item key="2"><Link to="/">Home</Link></Menu.Item>
                <Menu.Item key="3"><Link to="/ingredients/">Ingredients</Link></Menu.Item>
            </Menu>
        </Header>
        <Content style={{
            padding: '5em',
        }}>
            {this.props.children}
        </Content>
        <Footer>
            Made by John Doe, Jane Doe, and Nancy Drew for SomeHackathon 2018
        </Footer>
      </Layout>
    );
  }
}

export default HeaderContentFooter;
