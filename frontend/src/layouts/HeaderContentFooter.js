import React, { Component } from 'react';
import { Layout, Menu } from 'antd';
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
                <Menu.Item key="2">nav 1</Menu.Item>
                <Menu.Item key="3">nav 2</Menu.Item>
                <Menu.Item key="4">nav 3</Menu.Item>
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
